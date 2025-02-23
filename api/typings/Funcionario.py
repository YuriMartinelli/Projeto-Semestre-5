from pydantic import BaseModel


class FuncionarioModel(BaseModel):
    id_funcionario: Optional[int] = None
    nome: str
    matricula: str
    cpf: str
    telefone: str
    grupo: int
    senha: str
