from database.schemas.produto_schema import ProdutoSchema
from typings.Produto import ProdutoAtualizarModel, ProdutoModel
import db


session = db.Session()


async def model_get_produto():
    return session.query(ProdutoSchema).all()


async def model_cadastrar_produto(corpo: ProdutoModel):
    novo_produto = ProdutoSchema(**corpo.model_dump())
    session.add(novo_produto)
    session.commit()
    return {"Produto": f"produto cadastrado com sucesso! id: {novo_produto.id_produto}"}


async def model_get_produto_by_id(id: int):
    return session.query(ProdutoSchema).filter(ProdutoSchema.id_produto == id).first()


async def model_atualizar_produto(id: int, corpo: ProdutoAtualizarModel):
    CAMPOS_ATUALIZAR = {chave: valor for chave,
                        valor in corpo.model_dump().items() if valor is not None}
    session.query(ProdutoSchema).filter(
        ProdutoSchema.id_produto == id).update(CAMPOS_ATUALIZAR)

    return {"msg": f"Produto atualizado com sucesso! id: {id}"}


async def model_deletar_produto(id: int):
    session.query(ProdutoSchema).filter(
        ProdutoSchema.id_produto == id).delete()

    return {"msg": f"Produto deletado com sucesso! id: {id}"}
