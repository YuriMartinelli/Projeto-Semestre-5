from services.funcionario_service import servico_get_funcionario


async def controller_get_funcionario():
    return await servico_get_funcionario()
