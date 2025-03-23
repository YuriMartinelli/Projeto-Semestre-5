from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from controllers.produto_controller import (
    controller_atualizar_produto,
    controller_cadastar_produto,
    controller_deletar_produto,
    controller_get_produto,
    controller_get_produto_by_id
)
# Ajuste conforme seus tipos
from typings.Produto import ProdutoModel, ProdutoAtualizarModel
from services.auth_service import get_current_user
from db import get_db

produto_router = APIRouter(prefix="/produtos", tags=["Produto"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@produto_router.get("/consultar_produtos", status_code=status.HTTP_200_OK)
async def get_produto(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_get_produto()


@produto_router.get("/consultar_produto/{id}", status_code=status.HTTP_200_OK)
async def get_produto_by_id(id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_get_produto_by_id(id)


@produto_router.post("/criar_produto/", status_code=status.HTTP_201_CREATED)
async def post_produto(corpo: ProdutoModel, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_cadastar_produto(corpo)


@produto_router.put("/atualizar_produto/{id}", status_code=status.HTTP_200_OK)
async def put_produto(id: int, corpo: ProdutoAtualizarModel, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_atualizar_produto(id, corpo)


@produto_router.delete("/deletar_produto/{id}", status_code=status.HTTP_200_OK)
async def delete_produto(id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_deletar_produto(id)
