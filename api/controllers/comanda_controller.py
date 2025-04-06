from services.comanda_service import servico_atualizar_comanda, servico_cadastrar_comanda, servico_deletar_comanda, servico_get_comanda, servico_get_comanda_by_id
from typings.Comanda import ComandaModel


async def controller_cadastar_comanda(corpo: ComandaModel):
    return await servico_cadastrar_comanda(corpo)


async def controller_get_comanda():
    return await servico_get_comanda()


async def controller_get_comanda_by_id(id: int):
    return await servico_get_comanda_by_id(id)


async def controller_atualizar_comanda(id: int, corpo: ComandaModel):
    return await servico_atualizar_comanda(id, corpo)


async def controller_deletar_comanda(id: int):
    return await servico_deletar_comanda(id)
