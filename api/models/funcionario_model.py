from models.tables.funcionario_table import Funcionario
import db


session = db.Session()


async def model_get_funcionario():
    return session.query(Funcionario).all()
