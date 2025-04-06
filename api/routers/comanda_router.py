from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from controllers.comanda_controller import (
    controller_atualizar_comanda,
    controller_cadastar_comanda,
    controller_deletar_comanda,
    controller_get_comanda,
    controller_get_comanda_by_id
)
from typings.Comanda import ComandaModel, ComandaUpdateModel
# Importar o verificador de token
from services.auth_service import get_current_user
from db import get_db

# Yuri Martinelli
comanda_router = APIRouter(prefix="/comandas", tags=["Funcionário"])

# Esquema OAuth2 para extrair o token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@comanda_router.get("/consultar_comandas", status_code=status.HTTP_200_OK)
async def get_comanda(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_get_comanda()


@comanda_router.get("/consultar_comanda/{id}", status_code=status.HTTP_200_OK)
async def get_comanda_by_id(id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_get_comanda_by_id(id)


@comanda_router.post("/criar_comanda/", status_code=status.HTTP_201_CREATED)
async def post_comanda(corpo: ComandaModel, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_cadastar_comanda(corpo)


@comanda_router.put("/atualizar_comanda/{id}", status_code=status.HTTP_200_OK)
async def put_comanda(id: int, corpo: ComandaUpdateModel, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_atualizar_comanda(id, corpo)


@comanda_router.delete("/deletar_comanda/{id}", status_code=status.HTTP_200_OK)
async def delete_comanda(id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return await controller_deletar_comanda(id)
