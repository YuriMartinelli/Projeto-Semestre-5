from sqlite3 import OperationalError
from database.schemas.comanda_schema import ClienteSchema
from typings.Cliente import ClienteModel
import db


session = db.Session()


async def model_get_comanda():
    return session.query(ClienteSchema).all()


async def model_cadastrar_comanda(corpo: ClienteModel):
    novo_comanda = ClienteSchema(**corpo.model_dump())
    try:
        session.add(novo_comanda)
        session.commit()
        session.refresh(novo_comanda)
        session.rollback()
    except Exception as e:
        session.rollback()

        return {"msg": f"Erro ao cadastrar comanda: {e}, tente novemente"}
    return {"Cliente": f"comanda cadastrado com sucesso! id: {novo_comanda.id_comanda}"}


async def model_get_comanda_by_id(id: int):
    RESULT = session.query(ClienteSchema).filter(
        ClienteSchema.id_comanda == id).first()
    session.flush()
    return RESULT


async def model_atualizar_comanda(id: int, corpo: ClienteModel):
    VALORES_ATUALIZAR = {chave: valor for chave,
                         valor in corpo.model_dump().items() if valor is not None}

    session.query(ClienteSchema).filter(ClienteSchema.id_comanda == id).update(
        VALORES_ATUALIZAR)
    session.flush()
    return {"msg": f"Cliente atualizado com sucesso! id: {id}"}


async def model_deletar_comanda(id: int):
    session.query(ClienteSchema).filter(
        ClienteSchema.id_comanda == id).delete()
    session.flush()
    return {"msg": f"Cliente deletado com sucesso! id: {id}"}
