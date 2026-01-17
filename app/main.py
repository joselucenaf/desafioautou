from fastapi import FastAPI
from app.schemas import EmailRequest, EmailResponse
from app.nlp.preprocess import preprocess_text
from app.nlp.classifier import classify_email
from app.nlp.responder import generate_response

app = FastAPI(title="Email Classification API")

@app.post("/analyze-email", response_model=EmailResponse)
def analyze_email(request: EmailRequest):
    email_original = request.email
    email_limpo = preprocess_text(email_original)
    classificacao = classify_email(email_limpo)
    
    resposta = generate_response(
        email_original, 
        classificacao["categoria"]
    )

    return {
        "categoria": classificacao["categoria"],
        "confianca": classificacao["confianca"],
        "resposta_sugerida": resposta
    }