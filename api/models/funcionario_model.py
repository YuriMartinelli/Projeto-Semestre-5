from typings.Funcionario import FuncionarioModel
from api.database.schemas.funcionario_schema import FuncionarioTable
import db


session = db.Session()


async def model_get_funcionario():
    return session.query(FuncionarioTable).all()


async def model_post_funcionario(informacoes_funcionario: FuncionarioModel):
    novo_funcionario = FuncionarioTable(**informacoes_funcionario.model_dump())
    session.add(novo_funcionario)
    session.commit()
    return {"oi": "oi"}
