from models.cliente_model import model_atualizar_cliente, model_cadastrar_cliente, model_deletar_cliente, model_get_cliente, model_get_cliente_by_id
from typings.Cliente import ClienteModel


async def servico_cadastrar_cliente(corpo: ClienteModel):
    return await model_cadastrar_cliente(corpo)


async def servico_get_cliente():
    return await model_get_cliente()


async def servico_get_cliente_by_id(id: int):
    return await model_get_cliente_by_id(id)


async def servico_atualizar_cliente(id: int, corpo: ClienteModel):
    return await model_atualizar_cliente(id, corpo)


async def servico_deletar_cliente(id: int):
    return await model_deletar_cliente(id)
