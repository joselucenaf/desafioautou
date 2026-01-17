from pydantic import BaseModel

class EmailRequest(BaseModel):
    email: str

class EmailResponse(BaseModel):
    categoria: str
    confianca: float
    resposta_sugerida: str


#Centraliza a resposta e garante que o Frontend receba sempre a mesma estrutura, 
# independente de a análise ter sido feita via texto direto ou arquivo.