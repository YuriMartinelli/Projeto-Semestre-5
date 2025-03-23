from fastapi import APIRouter, Depends
from pydantic import BaseModel
from api.typings.Auth import LoginModel
from controllers.auth_controller import login_controller, criar_usuario_controller
from sqlalchemy.orm import Session
from db import get_db

router = APIRouter(prefix="/auth", tags=["autenticação"])


@router.post("/login")
def login(login_data: LoginModel, db: Session = Depends(get_db)):
    return login_controller(login_data.username, login_data.password, db)


@router.post("/usuarios")
def criar_usuario(usuario_data: UsuarioModel, db: Session = Depends(get_db)):
    return criar_usuario_controller(usuario_data.username, usuario_data.password, db)
