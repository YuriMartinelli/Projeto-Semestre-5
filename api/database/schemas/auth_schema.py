from sqlalchemy import Column, Integer, String
from db import Base


class Auth(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Senha hasheada
