from fastapi import FastAPI # type: ignore
from routes import translator_routes

app = FastAPI(
    title="Udaan LangBridge – Lightweight Translator API",
    description="An efficient translation microservice built with FastAPI. Supports real-time and bulk translation with logging.",
    version="1.0.1"
)

@app.get("/")
def root_endpoint():
    return {
        "message": "Welcome to Project Udaan – Translation Microservice 🚀",
        "docs": "Visit /docs for API documentation",
        "health": "/health"
    }

app.include_router(translator_routes.router)

