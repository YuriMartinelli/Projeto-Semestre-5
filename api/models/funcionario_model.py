from typings.Funcionario import FuncionarioModel
from database.schemas.funcionario_schema import FuncionarioTable
import db


session = db.Session()


async def model_get_funcionario():
    return session.query(FuncionarioTable).all()


async def model_post_funcionario(informacoes_funcionario: FuncionarioModel):
    novo_funcionario = FuncionarioTable(**informacoes_funcionario.model_dump())
    session.add(novo_funcionario)
    session.commit()
    return {"Funcionerio": f"Funcionario cadastrado com sucesso! id: {novo_funcionario.id_funcionario}"}


async def model_get_funcionario_by_id(id: int):
    return session.query(FuncionarioTable).filter(FuncionarioTable.id_funcionario == id).first()


async def model_atualizar_funcionario(id: int, corpo: FuncionarioModel):
    VALORES_ATUALIZAR = {chave: valor for chave,
                         valor in corpo.model_dump().items() if valor is not None}

    session.query(FuncionarioTable).filter(
        FuncionarioTable.id_funcionario == id).update(VALORES_ATUALIZAR)

    return {"msg": f"Funcionario atualizado com sucesso! id: {id}"}


async def model_deletar_funcionario(id: int):
    session.query(FuncionarioTable).filter(
        FuncionarioTable.id_funcionario == id).delete()

    return {"msg": f"Funcionario deletado com sucesso! id: {id}"}
