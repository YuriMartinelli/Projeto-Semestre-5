from sqlite3 import OperationalError
from database.schemas.comanda_schema import ComandaSchema
from typings.Comanda import ComandaModel
import db


session = db.Session()


async def model_get_comanda():
    return session.query(ComandaSchema).all()


async def model_cadastrar_comanda(corpo: ComandaModel):
    novo_comanda = ComandaSchema(**corpo.model_dump())
    try:
        session.add(novo_comanda)
        session.commit()
        session.refresh(novo_comanda)
        session.rollback()
    except Exception as e:
        session.rollback()

        return {"msg": f"Erro ao cadastrar comanda: {e}, tente novemente"}
    return {"Comanda": f"comanda cadastrado com sucesso! id: {novo_comanda.id_comanda}"}


async def model_get_comanda_by_id(id: int):
    RESULT = session.query(ComandaSchema).filter(
        ComandaSchema.id_comanda == id).first()
    session.flush()
    return RESULT


async def model_atualizar_comanda(id: int, corpo: ComandaModel):
    VALORES_ATUALIZAR = {chave: valor for chave,
                         valor in corpo.model_dump().items() if valor is not None}

    session.query(ComandaSchema).filter(ComandaSchema.id_comanda == id).update(
        VALORES_ATUALIZAR)
    session.flush()
    return {"msg": f"Comanda atualizado com sucesso! id: {id}"}


async def model_deletar_comanda(id: int):
    session.query(ComandaSchema).filter(
        ComandaSchema.id_comanda == id).delete()
    session.flush()
    return {"msg": f"Comanda deletado com sucesso! id: {id}"}
