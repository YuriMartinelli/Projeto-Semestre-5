from typings.Funcionario import FuncionarioModel
from models.funcionario_model import model_get_funcionario, model_post_funcionario


async def servico_get_funcionario():
    return await model_get_funcionario()


async def servico_post_funcionario(informacoes_funcionario: FuncionarioModel):
    return await model_post_funcionario(informacoes_funcionario)
