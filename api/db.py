from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configs.settings import STR_DATABASE

engine = create_engine(STR_DATABASE, echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()


def cria_tabelas():
    Base.metadata.create_all(engine, checkfirst=True)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
