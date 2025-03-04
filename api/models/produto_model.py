from database.schemas.produto_schema import ProdutoSchema
from typings.Produto import ProdutoModel
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


async def model_atualizar_produto(id: int, corpo: ProdutoModel):
    CLIENTE_ENCONTRADO = session.query(ProdutoSchema).filter(
        ProdutoSchema.id_produto == id).first()

    if not CLIENTE_ENCONTRADO:
        return {"msg": "Funcionario não encontrado"}

    for chave, valor in corpo.model_dump().items():
        setattr(CLIENTE_ENCONTRADO, chave, valor)

    session.commit()
    session.refresh()

    return {"msg": f"Funcionario atualizado com sucesso! id: {id}"}


async def model_deletar_produto(id: int):
    CLIENTE_ENCONTRADO = session.query(ProdutoSchema).filter(
        ProdutoSchema.id_produto == id).first()

    if not CLIENTE_ENCONTRADO:
        return {"msg": "Funcionario não encontrado"}

    session.delete(CLIENTE_ENCONTRADO)
    session.commit()

    return {"msg": f"Funcionario deletado com sucesso! id: {id}"}
