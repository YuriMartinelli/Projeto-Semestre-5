from models.comanda_model import model_atualizar_comanda, model_cadastrar_comanda, model_deletar_comanda, model_get_comanda, model_get_comanda_by_id
from typings.Comanda import ComandaModel


async def servico_cadastrar_comanda(corpo: ComandaModel):
    return await model_cadastrar_comanda(corpo)


async def servico_get_comanda():
    return await model_get_comanda()


async def servico_get_comanda_by_id(id: int):
    return await model_get_comanda_by_id(id)


async def servico_atualizar_comanda(id: int, corpo: ComandaModel):
    return await model_atualizar_comanda(id, corpo)


async def servico_deletar_comanda(id: int):
    return await model_deletar_comanda(id)
