from fastapi import APIRouter, status

from controllers.cliente_controller import controller_atualizar_cliente, controller_cadastar_cliente, controller_deletar_cliente, controller_get_cliente, controller_get_cliente_by_id
from typings.Cliente import ClienteModel, ClienteUpdateModel
# Yuri Martinelli
cliente_router = APIRouter(prefix="/clientes", tags=["Funcionário"])


@cliente_router.get("/consultar_clientes", status_code=status.HTTP_200_OK)
async def get_funcionario():
    return await controller_get_cliente()


@cliente_router.get("/consultar_cliente/{id}", status_code=status.HTTP_200_OK)
async def get_cliente(id: int):
    return await controller_get_cliente_by_id(id)


@cliente_router.post("/criar_cliente/", status_code=status.HTTP_201_CREATED)
async def post_cliente(corpo: ClienteModel):
    return await controller_cadastar_cliente(corpo)


@cliente_router.put("/atualizar_cliente/{id}", status_code=status.HTTP_200_OK)
async def put_cliente(id: int, corpo: ClienteUpdateModel):
    return await controller_atualizar_cliente(id, corpo)


@cliente_router.delete("/deletar_cliente/{id}", status_code=status.HTTP_200_OK)
async def delete_cliente(id: int):
    return await controller_deletar_cliente(id)
