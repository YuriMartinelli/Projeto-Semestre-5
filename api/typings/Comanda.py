import datetime
from typing import Optional
from pydantic import BaseModel


class ComandaModel(BaseModel):
    id_comanda: Optional[int]
    comanda: int
    data_hora: datetime
    status: str
    id_funcionario: int
    id_cliente: int
