import graphene
import uvicorn
from fastapi import FastAPI
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from starlette.middleware.cors import CORSMiddleware

from gql.Query import Query

app = FastAPI()
app.add_middleware(CORSMiddleware)

app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query),
                              executor_class=AsyncioExecutor))

if __name__ == "__main__":
    uvicorn.run(app)
