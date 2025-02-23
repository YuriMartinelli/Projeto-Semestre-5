from typing import Optional

from pydantic import BaseModel


class ProdutoModel(BaseModel):
    id: Optional[int]
    nome: str
    descricao: str
    foto: str
    valor_unitario: float
