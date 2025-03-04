from fastapi import FastAPI
import uvicorn
# Yuri Martinelli
from db import cria_tabelas
from configs.settings import HOST, PORT, RELOAD
from routers.main_router import main_router
from routers.funcionario_router import funcionario_router
from routers.cliente_router import cliente_router
from routers.produto_router import produto_router

app = FastAPI()

app.include_router(main_router)
app.include_router(funcionario_router)
app.include_router(cliente_router)
app.include_router(produto_router)

cria_tabelas()

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=RELOAD)
