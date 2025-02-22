from fastapi import APIRouter

router = APIRouter(prefix="/funcionarios")


@router.get("/consultar_funcionarios", tags=["Funcionário"])
def get_funcionario():
    return {"msg": "get todos executado"}, 200


@router.get("/consultar_funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    return {"msg": f"get um executado no id: {id}"}, 200


@router.post("/criar_funcionario/", tags=["Funcionário"])
def post_funcionario():
    return {"msg": "post executado"}, 200


@router.put("/atualizar_funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int):
    return {"msg": "put executado"}, 200


@router.delete("/deletar_funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 200
