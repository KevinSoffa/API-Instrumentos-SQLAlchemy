from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from core.database import Base


class Instrument(Base):
    __tablename__="instruments"

    id = Column(
        Integer,
        primary_key=True,
        index=False
    )
    nome = Column(
        String(100),
        nullable=False
    )
    marca = Column(
        String(50),
        nullable=False
    )
    preco = Column(
        Float,
        nullable=False
    )
    modelo = Column(
        String(50),
        nullable=False
    )
    orquestra = Column(
        Boolean, default=False
    )
    comentario = Column(
        Text,
        nullable=True
    )