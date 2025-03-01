from typings.Funcionario import FuncionarioModel
from services.funcionario_service import servico_get_funcionario, servico_post_funcionario


async def controller_get_funcionario():
    return await servico_get_funcionario()


async def controller_post_funcionario(informacoes_funcionario: FuncionarioModel):
    return await servico_post_funcionario(informacoes_funcionario)
