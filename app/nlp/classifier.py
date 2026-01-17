from transformers import pipeline

# Modelo zero-shot
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = ["Produtivo", "Improdutivo"]

def classify_email(text: str) -> dict:
    result = classifier(text, LABELS)

    return {
        "categoria": result["labels"][0],
        "confianca": round(result["scores"][0], 2)
    }
