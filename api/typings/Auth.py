from pydantic import BaseModel


class LoginModel(BaseModel):
    username: str
    password: str


class UsuarioModel(BaseModel):
    username: str
    password: str
