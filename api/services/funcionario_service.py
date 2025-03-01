from models.funcionario_model import model_get_funcionario


async def servico_get_funcionario():
    return await model_get_funcionario()
