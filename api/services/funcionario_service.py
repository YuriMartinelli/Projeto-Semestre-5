from typings.Funcionario import FuncionarioModel
from models.funcionario_model import model_atualizar_funcionario, model_deletar_funcionario, model_get_funcionario, model_get_funcionario_by_id, model_post_funcionario


async def servico_get_funcionario():
    return await model_get_funcionario()


async def servico_post_funcionario(informacoes_funcionario: FuncionarioModel):
    return await model_post_funcionario(informacoes_funcionario)


async def servico_get_funcionario_by_id(id: int):
    return await model_get_funcionario_by_id(id)


async def servico_atualizar_funcionario(id: int, corpo: FuncionarioModel):
    return await model_atualizar_funcionario(id, corpo)


async def servico_deletar_funcionario(id: int):
    return await model_deletar_funcionario(id)
