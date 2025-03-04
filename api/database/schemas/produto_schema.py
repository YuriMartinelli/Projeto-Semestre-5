from sqlalchemy import BLOB, FLOAT, VARCHAR, Column, Integer
from db import Base


class ProdutoSchema(Base):
    __tablename__ = 'tb_produto'

    id_produto = Column(Integer, primary_key=True,
                        autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(200), nullable=False)
    valor_unitario = Column(FLOAT(5, 2), nullable=False)
    foto = Column(BLOB(), nullable=True)
