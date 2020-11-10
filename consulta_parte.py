import re
from datetime import date
from typing import List
from urllib.parse import parse_qs, urlparse

import aiohttp
from bs4 import BeautifulSoup, Tag

import consulta_processo
from Comarca import Comarca
from Processo import Processo

URL_BASE = "http://www4.tjrj.jus.br/consultaProcessoNome/"
URL_NOME = URL_BASE + "ConsultaNome.do"
URL_CPF = URL_BASE + "consultaCPF.do"
URL_NAVEGACAO = URL_BASE + "ConsultaNome.do"


async def parse(
        nome_ou_cpf: str,
        session: aiohttp.ClientSession,
        **data,
) -> List[Processo]:
    data["acao"] = "consulta"
    data["descOrigem"] = "1ª Instância"
    data["origem"] = "1"
    data["descCompetencia"] = "Criminal"
    data["competencia"] = "04"
    if "pativos" in data:
        data["pativos"] = str(data["pativos"]).lower()
    today = date.today()
    if "anoInicio" not in data:
        data["anoInicio"] = today.year - 20
    if "anoFinal" not in data:
        data["anoFinal"] = today.year
    if re.match(
            r"((\d{3}\.){2}\d{3}|\d{2}\.\d{3}\.\d{3}/\d{4})-\d{2}",
            nome_ou_cpf
    ):
        data["numeroCpfCnpj"] = nome_ou_cpf
        if "comarca" not in data:
            data["comarca"] = Comarca.CAPITAL
        url = URL_CPF
    else:
        data["nomeParte"] = nome_ou_cpf
        if "comarca" not in data:
            data["comarca"] = Comarca.TODAS_COMARCAS
        url = URL_NOME
    data["descComarca"] = data["comarca"].name

    nums_processos: List[str] = []
    pagina = 1
    print("pagina =", pagina)
    resp: aiohttp.ClientResponse = await session.post(url, data=data)
    markup: bytes = await resp.read()
    content: Tag = BeautifulSoup(
        markup.decode("utf8", "mixed"), "lxml"
    ).find("div", id="content")
    tag: Tag = content.find("input", {"name": "totPagina"})
    tot_pagina = float(tag["value"])
    while True:
        tags: List[Tag] = content.find_all(
            "a",
            string=re.compile(r"\d{1,7}-\d{2}\.\d{4}\.\d\.?\d\d(\.\d{4})?"),
        )
        for tag in tags:
            nums_processos.append(
                parse_qs(urlparse(tag["href"]).query)["numProcesso"][0]
            )

        if pagina >= tot_pagina:
            break
        pagina += 1

        print("pagina =", pagina)
        resp = await session.post(
            URL_NAVEGACAO,
            data=dict(
                acao="navegacao",
                paginaAtual=pagina,
                totPagina=tot_pagina,
                privada=0,
                pagina=pagina,
            ),
        )
        markup = await resp.read()
        content: Tag = BeautifulSoup(
            markup.decode("utf8", "mixed"), "lxml"
        ).find("div", id="content")

    processos: List[Processo] = []
    for num_processo in nums_processos:
        processo = await consulta_processo.parse(num_processo, session)
        if processo is not None:
            processos.append(processo)
    return processos
