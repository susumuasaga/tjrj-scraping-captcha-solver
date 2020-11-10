from graphene import ObjectType, NonNull, String, ID


class Processo(ObjectType):
    numero = NonNull(ID)
    reu = NonNull(String)
