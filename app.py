from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Enterprise RAG Chatbot",
        "status": "Running"
    }
