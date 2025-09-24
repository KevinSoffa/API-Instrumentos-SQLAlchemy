from pydantic import BaseModel


class InstrumentBase(BaseModel):
    nome:str
    marca:str
    preco:float
    modelo:str
    orquestra:bool
    comentario:str

class InstrumentCreate(InstrumentBase):
    pass

class InstrumentUpdate(InstrumentBase):
    pass

class InstrumentResponse(InstrumentBase):
    id: int

    class Config:
        from_attributes = True  # substitui orm_mode=True no Pydantic v2