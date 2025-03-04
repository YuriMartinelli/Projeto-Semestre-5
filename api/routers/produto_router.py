from typing import Any
from fastapi import APIRouter, status

from controllers.produto_controller import controller_atualizar_produto, controller_cadastar_produto, controller_deletar_produto, controller_get_produto, controller_get_produto_by_id
from typings.Produto import ProdutoModel

produto_router = APIRouter(prefix="/produtos", tags=["Funcionário"])


@produto_router.get("/consultar_produtos", status_code=status.HTTP_200_OK)
async def get_produto():
    return await controller_get_produto()


@produto_router.get("/consultar_produto/{id}", status_code=status.HTTP_200_OK)
async def get_produto(id: int):
    return await controller_get_produto_by_id(id)


@produto_router.post("/criar_produto/", status_code=status.HTTP_201_CREATED)
async def post_produto(corpo: ProdutoModel):
    return await controller_cadastar_produto(corpo)


@produto_router.put("/atualizar_produto/{id}", status_code=status.HTTP_200_OK)
async def put_produto(id: int, corpo: Any):
    return await controller_atualizar_produto(id, corpo)


@produto_router.delete("/deletar_produto/{id}", status_code=status.HTTP_200_OK)
async def delete_produto(id: int):
    return await controller_deletar_produto(id)
