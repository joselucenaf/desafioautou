from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import fitz 
import os


from app.schemas import EmailRequest, EmailResponse
from app.nlp.classifier import classify_email
from app.nlp.responder import generate_response

app = FastAPI(title="Email Classification API", docs_url="/api/docs")

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_PATH = os.path.join(BASE_DIR, "..", "frontend")

if os.path.exists(FRONTEND_PATH):
    app.mount("/static", StaticFiles(directory=FRONTEND_PATH), name="static")

def process_logic(text: str):
    classificacao = classify_email(text) 
    resposta = generate_response(text, classificacao["categoria"])

    return {
        "categoria": classificacao["categoria"],
        "confianca": classificacao["confianca"],
        "resposta_sugerida": resposta
    }

@app.get("/")
async def serve_frontend():
    index_path = os.path.join(FRONTEND_PATH, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Backend rodando. Frontend não encontrado em: " + index_path}

@app.post("/analyze-email", response_model=EmailResponse)
def analyze_email(request: EmailRequest):
    return process_logic(request.email)

@app.post("/analyze-file", response_model=EmailResponse)
async def analyze_file(file: UploadFile = File(...)):
    content = ""
    file_bytes = await file.read()

    try:
        if file.filename.endswith(".txt"):
            content = file_bytes.decode("utf-8")
        elif file.filename.endswith(".pdf"):
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            for page in doc:
                content += page.get_text()
            doc.close()
        else:
            raise HTTPException(status_code=400, detail="Formato não suportado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar: {str(e)}")

    if not content.strip():
        raise HTTPException(status_code=400, detail="Arquivo sem texto legível.")
    
    return process_logic(content)

@app.get("/health")
def health_check():
    return {"status": "healthy"}