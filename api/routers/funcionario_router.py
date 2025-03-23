from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from controllers.funcionario_controller import (
    controller_atualizar_funcionario,
    controller_post_funcionario,
    controller_deletar_funcionario,
    controller_get_funcionario,
    controller_get_funcionario_by_id
)
# Ajuste conforme seus tipos
from typings.Funcionario import FuncionarioModel, FuncionarioAtualizarModel
from services.auth_service import get_current_user
from db import get_db

funcionario_router = APIRouter(prefix="/funcionarios", tags=["Funcionário"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@funcionario_router.get("/consultar_funcionarios", status_code=status.HTTP_200_OK)
async def get_funcionario(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_get_funcionario()


@funcionario_router.get("/consultar_funcionario/{id}", status_code=status.HTTP_200_OK)
async def get_funcionario_by_id(id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_get_funcionario_by_id(id)


@funcionario_router.post("/criar_funcionario/", status_code=status.HTTP_201_CREATED)
async def post_funcionario(corpo: FuncionarioModel, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_post_funcionario(corpo)


@funcionario_router.put("/atualizar_funcionario/{id}", status_code=status.HTTP_200_OK)
async def put_funcionario(id: int, corpo: FuncionarioAtualizarModel, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_atualizar_funcionario(id, corpo)


@funcionario_router.delete("/deletar_funcionario/{id}", status_code=status.HTTP_200_OK)
async def delete_funcionario(id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_deletar_funcionario(id)
