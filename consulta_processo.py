import re
from datetime import date
from typing import List
from urllib.parse import urljoin

import aiohttp
import cv2
import numpy as np
from bs4 import BeautifulSoup, Tag, NavigableString

import captcha_distortion
import noise_filter
import ocr
from Processo import Processo, Movimentacao, Advogado, Pessoa, MovimentacaoTipo

URL = "http://www4.tjrj.jus.br/consultaProcessoWebV2/consultaMov.do"
OAB_RE = r"([A-T]{2}\d*[A-P]?)"
NOME_RE = r"([^\s]*(?: [^\s]*)*)"


def find_all_fields(container: Tag, name: str, **kwargs) -> List[Tag]:
    return [
        tag.find_next_sibling("td")
        for tag in container.find_all(
            "td", string=re.compile(name, re.IGNORECASE), **kwargs
        )
    ]


async def parse(num_processo: str, session: aiohttp.ClientSession) -> Processo:
    print("num_processo =", num_processo)
    params = dict(
        v=2,
        numProcesso=num_processo,
        acessoIP="internet",
    )
    resp: aiohttp.ClientResponse = await session.get(URL, params=params)
    while True:
        markup: bytes = await resp.read()
        if len(markup) == 0:
            resp = await session.get(URL, params=params)
            markup = await resp.read()
        soup = BeautifulSoup(markup.decode("utf-8", "mixed"), "lxml")
        img_captcha_input: Tag = soup.find("input", id="imgCaptcha")
        if not img_captcha_input:
            break
        resp = await session.get(urljoin(URL, img_captcha_input["src"]))
        image = cv2.imdecode(
            np.asarray(bytearray(await resp.read()), dtype="uint8"),
            cv2.IMREAD_GRAYSCALE,
        )
        captcha, _ = ocr.read(
            noise_filter.clean(captcha_distortion.undistort(image))
        )
        print("captcha =", captcha)
        resp = await session.post(
            URL,
            params=params,
            data=dict(captcha=captcha, numProcesso=num_processo),
        )

    content: Tag = soup.find("div", id="content")
    classe_tags = find_all_fields(content, "classe", class_="info")
    processo = dict(
        classe=classe_tags[0].get_text(strip=True),
        reus=[],
        movimentacoes=[],
        advogados=[],
    )
    if not re.match(
            "ação penal|procedimento especial",
            processo["classe"],
            re.IGNORECASE
    ):
        return

    tag: Tag = content.find("input", {"name": "codigoProc"})
    processo["numero"] = tag["value"]

    tag = content.find(
        "td", class_="info", string=re.compile(
            "comarca|regional", re.IGNORECASE
        )
    )
    processo["comarca"] = tag.get_text(strip=True)

    tag = content.find(
        "td", class_="info", string=re.compile("vara", re.IGNORECASE)
    )
    processo["vara"] = tag.get_text(strip=True)

    processo["assunto"] = (
        find_all_fields(
            content, "assunto", class_="info"
        )[0].get_text(strip=True)
    )

    tag = content.find(
        string=re.compile("listar todos os personagens", re.IGNORECASE)
    )
    if tag is None:
        processo["autor"] = (
            find_all_fields(
                content, "autor", class_="info"
            )[0].get_text(strip=True)
        )

        tags = find_all_fields(
            content, "acusado|indiciado|denunciado|réu", class_="info"
        )
        if len(tags) == 0:
            return
        processo["reus"].append(Pessoa(nome=(tags[0].get_text(strip=True))))

        tags = find_all_fields(content, "advogado", class_="info")
        if len(tags) == 0:
            return
        contents = tags[0].contents
        # advogados estão em contents[0::2]
        i = 0
        while i < len(contents):
            match = re.match(
                r"\s*" + OAB_RE + r"\s*-\s*" + NOME_RE, contents[i]
            )
            if not match:
                break
            processo["advogados"].append(
                Advogado(oab=match.group(1), nome=match.group(2))
            )
            i += 2

    else:
        lista_personagens: Tag = content.find("div", id="listaPersonagens")

        processo["autor"] = (
            find_all_fields(
                lista_personagens, "autor", class_="tab-titulo-bold"
            )[0].get_text(strip=True)
        )

        processo["reus"] = [
            Pessoa(nome=tag.get_text(strip=True))
            for tag in find_all_fields(
                lista_personagens,
                "acusado|indiciado|denunciado|réu",
                class_="tab-titulo-bold",
            )
        ]

        tags = find_all_fields(
            lista_personagens, "advogado", class_="tab-titulo-bold",
        )
        for tag in tags:
            match = re.match(
                r"\s*\(" + OAB_RE + r"\)\s*" + NOME_RE,
                tag.get_text(strip=True),
            )
            processo["advogados"].append(
                Advogado(oab=match.group(1), nome=match.group(2))
            )

    tags = find_all_fields(content, "tipo do movimento", class_="negrito")
    for tag in tags:
        movimentacao = dict(titulo=tag.get_text(strip=True))
        match = re.match(
            "despacho|decisão|sentença",
            movimentacao["titulo"],
            re.IGNORECASE,
        )
        if not match:
            continue

        tipo: str = match.group()
        movimentacao["tipo"] = MovimentacaoTipo(tipo.lower())

        row: Tag = tag.parent
        table: Tag = soup.new_tag("table")
        while True:
            sibling = row.next_sibling
            table.append(row)

            row = sibling
            if row is None or (
                    not isinstance(row, NavigableString)
                    and row.has_attr("class")
                    and "tipoMovimento" in row["class"]
            ):
                break

        string = table.find(
            string=re.compile("ver íntegra", re.IGNORECASE)
        )
        if string is None:
            continue

        match = re.match(
            r"(\d{1,2})/(\d{1,2})/(\d{4})",
            find_all_fields(
                table, "data", class_="negrito"
            )[0].get_text(strip=True),
        )
        movimentacao["data"] = date(
            int(match.group(3)),
            int(match.group(2)),
            int(match.group(1)),
        )

        movimentacao["resumo"] = find_all_fields(
            table, "descrição", class_="negrito"
        )[0].contents[0].strip()

        integra_tag: Tag = table.find("input", {"name": re.compile("descMov")})
        movimentacao["integra"] = integra_tag["value"]

        processo["movimentacoes"].append(Movimentacao(**movimentacao))
    return Processo(**processo)
