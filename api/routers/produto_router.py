from fastapi import APIRouter, status

from typings.Produto import ProdutoModel

produto_router = APIRouter(prefix="/produtos", tags=["Funcionário"])


@produto_router.get("/consultar_produtos", status_code=status.HTTP_200_OK)
async def get_produto():
    return {"msg": "get todos executado"}


@produto_router.get("/consultar_produto/{id}", status_code=status.HTTP_200_OK)
async def get_produto(id: int):
    return {"msg": f"get um executado no id: {id}"}


@produto_router.post("/criar_produto/", status_code=status.HTTP_201_CREATED)
async def post_produto(corpo: ProdutoModel):
    return {"msg": "post executado", "nome": corpo.nome, "descricao": corpo.descricao, "valor_unitario": corpo.valor_unitario}


@produto_router.put("/atualizar_produto/{id}", status_code=status.HTTP_200_OK)
async def put_produto(id: int, corpo: ProdutoModel):
    return {"msg": "put executado", "id": id, "nome": corpo.nome, "descricao": corpo.descricao, "valor_unitario": corpo.valor_unitario}


@produto_router.delete("/deletar_produto/{id}", status_code=status.HTTP_200_OK)
async def delete_produto(id: int):
    return {"msg": "delete executado"}
