from fastapi import APIRouter

funcionario_router = APIRouter(prefix="/funcionarios")


@funcionario_router.get("/consultar_funcionarios", tags=["Funcionário"])
def get_funcionario():
    return {"msg": "get todos executado"}, 200


@funcionario_router.get("/consultar_funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    return {"msg": f"get um executado no id: {id}"}, 200


@funcionario_router.post("/criar_funcionario/", tags=["Funcionário"])
def post_funcionario():
    return {"msg": "post executado"}, 200


@funcionario_router.put("/atualizar_funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int):
    return {"msg": "put executado"}, 200


@funcionario_router.delete("/deletar_funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 200
