from sqlalchemy.orm import Session
from services.auth_service import authenticate_user, create_access_token, criar_usuario
from fastapi import Depends, HTTPException
from db import get_db


def login_controller(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


def criar_usuario_controller(username: str, password: str, db: Session = Depends(get_db)):
    try:
        usuario = criar_usuario(db, username, password)
        return {"msg": f"Usuário {usuario.username} criado com sucesso!"}
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Erro ao criar usuário: {str(e)}")
