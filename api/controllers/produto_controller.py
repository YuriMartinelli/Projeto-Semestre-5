from services.produto_service import servico_atualizar_produto, servico_cadastrar_produto, servico_deletar_produto, servico_get_produto, servico_get_produto_by_id
from typings.Produto import ProdutoModel


async def controller_cadastar_produto(corpo: ProdutoModel):
    return await servico_cadastrar_produto(corpo)


async def controller_get_produto():
    return await servico_get_produto()


async def controller_get_produto_by_id(id: int):
    return await servico_get_produto_by_id(id)


async def controller_atualizar_produto(id: int, corpo: ProdutoModel):
    return await servico_atualizar_produto(id, corpo)


async def controller_deletar_produto(id: int):
    return await servico_deletar_produto(id)
