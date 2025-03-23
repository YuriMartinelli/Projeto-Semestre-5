from sqlalchemy import Column, DateTime, Integer, String
from db import Base


class ComandaSchema(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    comanda = Column(String, nullable=False)
    data_hora = Column(DateTime, nullable=False)
    status = Column(String(4), nullable=False)
    id_funcionario = Column(String, unique=True, nullable=False,
                            foreign_key=True, reference="funcionarios.id")
    id_cliente = Column(String, unique=True, nullable=True,
                        foreign_key=True, reference="clientes.id")
