from services.cliente_service import servico_atualizar_cliente, servico_cadastrar_cliente, servico_deletar_cliente, servico_get_cliente, servico_get_cliente_by_id
from typings.Cliente import ClienteModel


async def controller_cadastar_cliente(corpo: ClienteModel):
    return await servico_cadastrar_cliente(corpo)


async def controller_get_cliente():
    return await servico_get_cliente()


async def controller_get_cliente_by_id(id: int):
    return await servico_get_cliente_by_id(id)


async def controller_atualizar_cliente(id: int, corpo: ClienteModel):
    return await servico_atualizar_cliente(id, corpo)


async def controller_deletar_cliente(id: int):
    return await servico_deletar_cliente(id)
