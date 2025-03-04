from typings.Funcionario import FuncionarioModel
from services.funcionario_service import servico_atualizar_funcionario, servico_deletar_funcionario, servico_get_funcionario, servico_get_funcionario_by_id, servico_post_funcionario


async def controller_get_funcionario():
    return await servico_get_funcionario()


async def controller_post_funcionario(informacoes_funcionario: FuncionarioModel):
    return await servico_post_funcionario(informacoes_funcionario)


async def controller_get_funcionario_by_id(id: int):
    return await servico_get_funcionario_by_id(id)


async def controller_atualizar_funcionario(id: int, corpo: FuncionarioModel):
    return await servico_atualizar_funcionario(id, corpo)


async def controller_deletar_funcionario(id: int):
    return await servico_deletar_funcionario(id)
