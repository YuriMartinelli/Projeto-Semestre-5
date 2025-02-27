from fastapi import APIRouter, status

from typings.Funcionario import FuncionarioModel

funcionario_router = APIRouter(prefix="/funcionarios", tags=["Funcionário"])


@funcionario_router.get("/consultar_funcionarios", status_code=status.HTTP_200_OK)
def get_funcionario():
    return {"msg": "get todos executado"}


@funcionario_router.get("/consultar_funcionario/{id}", status_code=status.HTTP_200_OK)
def get_funcionario(id: int):
    return {"msg": f"get um executado no id: {id}"}


@funcionario_router.post("/criar_funcionario/", status_code=status.HTTP_201_CREATED)
def post_funcionario(corpo: FuncionarioModel):
    return {"msg": "post executado", "nome": corpo.nome, "cpf": corpo.cpf, "telefone": corpo.telefone}


def put_funcionario(id: int, corpo: FuncionarioModel):
    return {"msg": "put executado", "id": id, "nome": corpo.nome, "cpf": corpo.cpf, "telefone": corpo.telefone}


@funcionario_router.delete("/deletar_funcionario/{id}", status_code=status.HTTP_200_OK)
def delete_funcionario(id: int):
    return {"msg": "delete executado"}
