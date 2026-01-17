from pydantic import BaseModel

class EmailRequest(BaseModel):
    email: str

class EmailResponse(BaseModel):
    categoria: str
    confianca: float
    resposta_sugerida: str
