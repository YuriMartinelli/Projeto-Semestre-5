from sqlalchemy import CHAR, VARCHAR, Column, Integer
from db import Base


class ClienteSchema(Base):
    __tablename__ = 'tb_cliente'

    id_cliente = Column(Integer, primary_key=True,
                        autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    cpf = Column(CHAR(11), unique=True, nullable=False, index=True)
    telefone = Column(CHAR(11), nullable=False)
