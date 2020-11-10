import asyncio
from datetime import date
from snapshottest.module import SnapshotTest
import pytest

import consulta_parte
import consulta_processo
from Comarca import Comarca
from FakeSession import FakeSession
from Processo import Processo, Advogado, Movimentacao, MovimentacaoTipo, Pessoa
from mixed_decoder import mixed_decoder
import codecs

pytestmark = pytest.mark.asyncio
codecs.register_error("mixed", mixed_decoder)
session = FakeSession()


@pytest.fixture()
def mock_processo(monkeypatch):
    async def fake_processo_parse(num_processo: str, session) -> Processo:
        await asyncio.sleep(0)
        return Processo(
            numero=num_processo,
            comarca="Comarca da Capital",
            vara="1ª Vara Criminal",
            classe="Ação Penal - Procedimento Ordinário",
            assunto="Estelionato (Art. 171 - CP)",
            autor="MINISTÉRIO PÚBLICO DO ESTADO DO RIO DE JANEIRO",
            reus=[Pessoa(nome="Luiz Fernando da Costa")],
            advogados=[Advogado(oab="RJ696969", nome="Beltrano da Silva")],
            movimentacoes=[
                Movimentacao(
                    tipo=MovimentacaoTipo.DECISAO,
                    data=date(2020, 2, 24),
                    titulo="Decisão - Recebimento de Denúncia",
                    resumo="Lorem ipsum dolor sit amet",
                    integra=(
                        "Lorem ipsum dolor sit amet, "
                        "consectetur adipiscing elit, "
                        "sed do eiusmod tempor incididunt ut labore "
                        "et dolore magna aliqua."
                    ),
                ),
            ],
        )

    monkeypatch.setattr(consulta_processo, "parse", fake_processo_parse)


async def test_consulta_ficha_limpa(snapshot: SnapshotTest, mock_processo):
    assert len(await consulta_parte.parse("Fulano da Silva", session)) == 0


async def test_consulta_nome(snapshot: SnapshotTest, mock_processo):
    snapshot.assert_match(
        [
            processo.dict()
            for processo in await consulta_parte.parse(
                "Luiz Fernando da Costa", session
            )
        ]
    )


async def test_consulta_cpf(snapshot: SnapshotTest, mock_processo):
    snapshot.assert_match(
        [
            processo.dict()
            for processo in await consulta_parte.parse(
                "28.305.936/0001-40",
                session,
                comarca=Comarca.QUEIMADOS,
                anoInicio=2010,
                anoFinal=2010,
                pativos=True,
            )
        ]
    )
