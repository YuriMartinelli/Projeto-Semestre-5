from typing import Optional
from pydantic import BaseModel


class ClienteModel(BaseModel):
    id_cliente: Optional[int] = None
    nome: str
    cpf: str
    telefone: str
