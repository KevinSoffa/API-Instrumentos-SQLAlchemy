# main.py

from fastapi import FastAPI
from fastapi.security import HTTPBearer
from core.database import Base, engine
from controller import instrument_controller, auth_controller

# Criar as tabelas
Base.metadata.create_all(bind=engine)

# Crie uma instância do HTTPBearer para o Swagger
security_scheme = {"bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}}

app = FastAPI(
    title="Instrumentos API",
    description="API com autenticação via JWT",
    version="1.0.0",
    # Adicione o esquema de segurança
    openapi_extra={"components": {"securitySchemes": security_scheme}}
)

# Rotas
app.include_router(auth_controller.router)
app.include_router(instrument_controller.router)