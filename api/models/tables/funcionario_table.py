from sqlalchemy import CHAR, VARCHAR, Column, Integer
import db


class FuncionarioTable(db.Base):
    __tablename__ = 'tb_funcionario'

    id_funcionario = Column(Integer, primary_key=True,
                            autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    matricula = Column(CHAR(10), nullable=False)
    cpf = Column(CHAR(11), unique=True, nullable=False, index=True)
    telefone = Column(CHAR(11), nullable=False)
    grupo = Column(Integer, nullable=False)
    senha = Column(VARCHAR(200), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, id_funcionario, nome, matricula, cpf, telefone, grupo, senha):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.telefone = telefone
        self.grupo = grupo
        self.senha = senha
