import re
from typing import Mapping

import aiofiles

import consulta_parte
import consulta_processo


class FakeClientResponse:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    async def read(self):
        async with aiofiles.open(self.filename, "rb") as file:
            return await file.read()


class FakeSession:
    captchas = ["toqnzad", "327gv25"]

    def __init__(self):
        self.captcha_no = 0
        self.nome_ou_cpf: str = None

    async def get(self, url: str, *, params: Mapping = None):
        if url == consulta_processo.URL:
            return FakeClientResponse("Consulta Captcha.html")
        else:
            # get captcha image
            return FakeClientResponse(
                f"./data/captcha_{self.get_captcha()}.png"
            )

    async def post(
            self, url: str, *, data: Mapping = None, params: Mapping = None
    ):
        if url.startswith(consulta_parte.URL_BASE):
            if data["acao"] == "consulta":
                if url == consulta_parte.URL_NOME:
                    self.nome_ou_cpf = data["nomeParte"]
                else:
                    # url = consulta_parte.URL_CPF
                    self.nome_ou_cpf = re.sub(
                        r"/\d{4}", "", data["numeroCpfCnpj"]
                    )
                pagina = 1
            else:
                # data["acao"] = "navegacao"
                pagina = data["paginaAtual"]
            resp = FakeClientResponse(
                f"processos-{self.nome_ou_cpf}-{pagina}.html"
            )
        else:
            # captcha sent
            if data["captcha"] == self.get_captcha():
                resp = FakeClientResponse(f"processo{data['numProcesso']}.html")
            else:
                resp = FakeClientResponse("wrong captcha.html")
            self.captcha_no += 1
            if self.captcha_no >= len(self.captchas):
                self.captcha_no = 0

        return resp

    def get_captcha(self):
        return self.captchas[self.captcha_no]
