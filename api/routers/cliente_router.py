from fastapi import APIRouter, status

cliente_router = APIRouter(prefix="/clientes", tags=["Funcionário"])


@cliente_router.get("/consultar_clientes", status_code=status.HTTP_200_OK)
def get_funcionario():
    return {"msg": "get todos executado"}


@cliente_router.get("/consultar_cliente/{id}", status_code=status.HTTP_200_OK)
def get_cliente(id: int):
    return {"msg": f"get um executado no id: {id}"}


@cliente_router.post("/criar_cliente/", status_code=status.HTTP_201_CREATED)
def post_cliente():
    return {"msg": "post executado"}


@cliente_router.put("/atualizar_cliente/{id}", status_code=status.HTTP_200_OK)
def put_cliente(id: int):
    return {"msg": "put executado"}


@cliente_router.delete("/deletar_cliente/{id}", status_code=status.HTTP_200_OK)
def delete_cliente(id: int):
    return {"msg": "delete executado"}
