from typing import Optional
from pydantic import BaseModel


class FuncionarioModel(BaseModel):
    id_funcionario: Optional[int] = None
    nome: str
    matricula: str
    cpf: str
    telefone: str
    grupo: int
    senha: str


class FuncionarioAtualizarModel(BaseModel):
    nome: Optional[str] = None
    matricula: Optional[str] = None
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    grupo: Optional[int] = None
    senha: Optional[str] = None
