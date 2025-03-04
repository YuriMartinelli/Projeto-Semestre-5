from database.schemas.cliente_schema import ClienteSchema
from typings.Cliente import ClienteModel
import db


session = db.Session()


async def model_get_cliente():
    return session.query(ClienteSchema).all()


async def model_cadastrar_cliente(corpo: ClienteModel):
    novo_cliente = ClienteSchema(**corpo.model_dump())
    session.add(novo_cliente)
    session.commit()
    return {"Cliente": f"cliente cadastrado com sucesso! id: {novo_cliente.id_cliente}"}


async def model_get_cliente_by_id(id: int):
    return session.query(ClienteSchema).filter(ClienteSchema.id_cliente == id).first()


async def model_atualizar_cliente(id: int, corpo: ClienteModel):
    CLIENTE_ENCONTRADO = session.query(ClienteSchema).filter(
        ClienteSchema.id_cliente == id).first()

    if not CLIENTE_ENCONTRADO:
        return {"msg": "Funcionario não encontrado"}

    for chave, valor in corpo.model_dump().items():
        setattr(CLIENTE_ENCONTRADO, chave, valor)

    session.commit()
    session.refresh()

    return {"msg": f"Funcionario atualizado com sucesso! id: {id}"}


async def model_deletar_cliente(id: int):
    CLIENTE_ENCONTRADO = session.query(ClienteSchema).filter(
        ClienteSchema.id_cliente == id).first()

    if not CLIENTE_ENCONTRADO:
        return {"msg": "Funcionario não encontrado"}

    session.delete(CLIENTE_ENCONTRADO)
    session.commit()

    return {"msg": f"Funcionario deletado com sucesso! id: {id}"}
