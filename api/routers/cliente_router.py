from fastapi import APIRouter, status

from typings.Cliente import ClienteModel, ClienteUpdateModel
# Yuri Martinelli
cliente_router = APIRouter(prefix="/clientes", tags=["Funcionário"])


@cliente_router.get("/consultar_clientes", status_code=status.HTTP_200_OK)
async def get_funcionario():
    return {"msg": "get todos executado"}


@cliente_router.get("/consultar_cliente/{id}", status_code=status.HTTP_200_OK)
async def get_cliente(id: int):
    return {"msg": f"get um executado no id: {id}"}


@cliente_router.post("/criar_cliente/", status_code=status.HTTP_201_CREATED)
async def post_cliente(corpo: ClienteModel):
    return {"msg": "post executado", "nome": corpo.nome, "cpf": corpo.cpf, "telefone": corpo.telefone}


@cliente_router.put("/atualizar_cliente/{id}", status_code=status.HTTP_200_OK)
async def put_cliente(id: int, corpo: ClienteUpdateModel):
    return {"msg": "put executado", "id": id, "nome": corpo.nome, "cpf": corpo.cpf, "telefone": corpo.telefone}


@cliente_router.delete("/deletar_cliente/{id}", status_code=status.HTTP_200_OK)
async def delete_cliente(id: int):
    return {"msg": "delete executado"}
