from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typings.Auth import LoginModel, UsuarioModel
from controllers.auth_controller import login_controller, criar_usuario_controller
from sqlalchemy.orm import Session
from db import get_db

auth_router = APIRouter(prefix="/auth", tags=["autenticação"])


@auth_router.post("/login")
def login(login_data: LoginModel, db: Session = Depends(get_db)):
    return login_controller(login_data.username, login_data.password, db)


@auth_router.post("/usuarios")
def criar_usuario(usuario_data: UsuarioModel, db: Session = Depends(get_db)):
    print("oi")
    return criar_usuario_controller(usuario_data.username, usuario_data.password, db)
