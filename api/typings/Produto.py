from typing import Optional

from pydantic import BaseModel


class ProdutoModel(BaseModel):
    id_produto: Optional[int] = None
    nome: str
    descricao: str
    foto: Optional[str] = None
    valor_unitario: float


class ProdutoAtualizarModel(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    foto: Optional[str] = None
    valor_unitario: Optional[float] = None
