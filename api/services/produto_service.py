from models.produto_model import model_atualizar_produto, model_cadastrar_produto, model_deletar_produto, model_get_produto, model_get_produto_by_id
from typings.Produto import ProdutoModel


async def servico_cadastrar_produto(corpo: ProdutoModel):
    return await model_cadastrar_produto(corpo)


async def servico_get_produto():
    return await model_get_produto()


async def servico_get_produto_by_id(id: int):
    return await model_get_produto_by_id(id)


async def servico_atualizar_produto(id: int, corpo: ProdutoModel):
    return await model_atualizar_produto(id, corpo)


async def servico_deletar_produto(id: int):
    return await model_deletar_produto(id)
