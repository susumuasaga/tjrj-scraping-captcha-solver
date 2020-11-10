from datetime import date
from typing import List

from pydantic import BaseModel

from StrEnum import StrEnum


class MovimentacaoTipo(str, StrEnum):
    DESPACHO = "despacho"
    DECISAO = "decisão"
    SENTENCA = "sentença"


class Movimentacao(BaseModel):
    tipo: MovimentacaoTipo
    titulo: str
    data: date
    resumo: str
    integra: str = None


class Pessoa(BaseModel):
    nome: str
    cpf: str = None


class Advogado(BaseModel):
    oab: str
    nome: str


class Processo(BaseModel):
    numero: str
    comarca: str
    vara: str
    assunto: str
    classe: str
    autor: str
    reus: List[Pessoa] = []
    advogados: List[Advogado] = []
    movimentacoes: List[Movimentacao] = []
