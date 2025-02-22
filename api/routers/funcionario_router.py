from fastapi import APIRouter, status

funcionario_router = APIRouter(prefix="/funcionarios", tags=["Funcionário"])


@funcionario_router.get("/consultar_funcionarios", status_code=status.HTTP_200_OK)
def get_funcionario():
    return {"msg": "get todos executado"}


@funcionario_router.get("/consultar_funcionario/{id}", status_code=status.HTTP_200_OK)
def get_funcionario(id: int):
    return {"msg": f"get um executado no id: {id}"}


@funcionario_router.post("/criar_funcionario/", status_code=status.HTTP_201_CREATED)
def post_funcionario():
    return {"msg": "post executado"}


@funcionario_router.put("/atualizar_funcionario/{id}", status_code=status.HTTP_200_OK)
def put_funcionario(id: int):
    return {"msg": "put executado"}


@funcionario_router.delete("/deletar_funcionario/{id}", status_code=status.HTTP_200_OK)
def delete_funcionario(id: int):
    return {"msg": "delete executado"}
