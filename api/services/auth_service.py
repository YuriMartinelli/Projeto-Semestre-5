from sqlalchemy.orm import Session

from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status

from database.schemas.auth_schema import Auth

# Configurações JWT
SECRET_KEY = "sua_chave_secreta_aqui"  # Gere com: openssl rand -hex 32
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração para hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + \
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(db: Session, username: str, password: str) -> Auth:
    user = db.query(Auth).filter(Auth.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    return user


def criar_usuario(db: Session, username: str, password: str) -> Auth:
    hashed_password = get_password_hash(password)
    novo_usuario = Auth(username=username, password=hashed_password)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario
