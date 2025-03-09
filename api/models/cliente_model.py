from sqlite3 import OperationalError
from database.schemas.cliente_schema import ClienteSchema
from typings.Cliente import ClienteModel
import db


session = db.Session()


async def model_get_cliente():
    return session.query(ClienteSchema).all()


async def model_cadastrar_cliente(corpo: ClienteModel):
    novo_cliente = ClienteSchema(**corpo.model_dump())
    try:
        session.add(novo_cliente)
        session.commit()
        session.refresh(novo_cliente)
    except (OperationalError) as e:
        session.rollback()
        session.flush()
        return {"msg": f"Erro ao cadastrar cliente: {e}, tente novemente"}
    return {"Cliente": f"cliente cadastrado com sucesso! id: {novo_cliente.id_cliente}"}


async def model_get_cliente_by_id(id: int):
    RESULT = session.query(ClienteSchema).filter(
        ClienteSchema.id_cliente == id).first()
    session.flush()
    return RESULT


async def model_atualizar_cliente(id: int, corpo: ClienteModel):
    VALORES_ATUALIZAR = {chave: valor for chave,
                         valor in corpo.model_dump().items() if valor is not None}

    session.query(ClienteSchema).filter(ClienteSchema.id_cliente == id).update(
        VALORES_ATUALIZAR)
    session.flush()
    return {"msg": f"Cliente atualizado com sucesso! id: {id}"}


async def model_deletar_cliente(id: int):
    session.query(ClienteSchema).filter(
        ClienteSchema.id_cliente == id).delete()
    session.flush()
    return {"msg": f"Cliente deletado com sucesso! id: {id}"}
