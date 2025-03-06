from fastapi import APIRouter, status

from controllers.funcionario_controller import controller_atualizar_funcionario, controller_deletar_funcionario, controller_get_funcionario, controller_get_funcionario_by_id, controller_post_funcionario
from typings.Funcionario import FuncionarioAtualizarModel, FuncionarioModel

funcionario_router = APIRouter(prefix="/funcionarios", tags=["Funcionário"])


@funcionario_router.get("/consultar_funcionarios", status_code=status.HTTP_200_OK)
async def get_funcionario():
    return await controller_get_funcionario()


@funcionario_router.get("/consultar_funcionario/{id}", status_code=status.HTTP_200_OK)
async def get_funcionario(id: int):  # -> Any:
    return await controller_get_funcionario_by_id(id)


@funcionario_router.post("/criar_funcionario/", status_code=status.HTTP_201_CREATED)
async def post_funcionario(informacoes_funcionario: FuncionarioModel):
    return await controller_post_funcionario(informacoes_funcionario)


@funcionario_router.put("/atualizar_funcionario/{id}", status_code=status.HTTP_200_OK)
async def put_funcionario(id: int, corpo: FuncionarioAtualizarModel):
    return await controller_atualizar_funcionario(id, corpo)


@funcionario_router.delete("/deletar_funcionario/{id}", status_code=status.HTTP_200_OK)
async def delete_funcionario(id: int):
    return await controller_deletar_funcionario(id)
