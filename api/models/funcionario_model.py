from api.db import db
from tables.funcionario_table import Funcionario

session = db.Session()


async def model_get_funcionario():
    return session.query(Funcionario).all()
