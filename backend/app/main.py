from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router
from app.core.config import Settings
from app.core.errors import register_errors
from app.core.logging import register_logging

def create_app():
    settings = Settings()
    app = FastAPI(title="HackerGazer API", version="0.1.0")
    app.include_router(router)
    register_errors(app)
    register_logging(app)
    app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type", "Idempotency-Key"], expose_headers=["X-Request-ID"])
    return app

app = create_app()
