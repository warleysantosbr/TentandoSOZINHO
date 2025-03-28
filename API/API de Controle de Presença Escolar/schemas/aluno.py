from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    idade: int
    matricula: str
    turma: str


class AlunoCreate(AlunoBase):
    pass


class AlunoResponse(AlunoBase):
    id: int

    class Config:
        from_attributes = True  
