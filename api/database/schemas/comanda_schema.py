from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from db import Base


class ComandaSchema(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    comanda = Column(String, nullable=False)
    data_hora = Column(DateTime, nullable=False)
    status = Column(String(4), nullable=False)
    id_funcionario = Column(String, ForeignKey(
        "funcionarios.id_funcionario"), unique=True, nullable=False)
    id_cliente = Column(String, ForeignKey(
        "clientes.id_cliente"), unique=True, nullable=True)
