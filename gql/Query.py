import asyncio

from graphene import ObjectType, NonNull, List, String
from starlette.requests import Request

from gql.Processo import Processo


class Query(ObjectType):
    processos = NonNull(List(NonNull(Processo)), nome_ou_cpf=NonNull(String))

    @staticmethod
    async def resolve_processos(root, info, nome_ou_cpf):
        request: Request = info.context["request"]
        await asyncio.sleep(0)
        return [dict(numero="1", reu=nome_ou_cpf)]
