from pydantic import BaseModel, ConfigDict
from typing import Optional


class InstrumentBase(BaseModel):
    nome: str
    marca: str
    preco: float
    modelo: str
    orquestra: bool
    comentario: str

class InstrumentCreate(InstrumentBase):
    pass

class InstrumentUpdate(BaseModel):
    nome: Optional[str] = None
    marca: Optional[str] = None
    preco: Optional[float] = None
    modelo: Optional[str] = None
    orquestra: Optional[bool] = None
    comentario: Optional[str] = None

class InstrumentResponse(InstrumentBase):
    id: int

    # Use ConfigDict no lugar da classe Config
    model_config = ConfigDict(from_attributes=True)