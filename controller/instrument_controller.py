from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.database import SessionLocal
from schema.instrument_schema import InstrumentCreate, InstrumentUpdate, InstrumentResponse
from service import instrument_service
from core.auth import get_current_user  # Função que valida o JWT

router = APIRouter(prefix="/instruments", tags=["Instruments"])

# Dependency para abrir/fechar conexão com o DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=InstrumentResponse, status_code=status.HTTP_201_CREATED)
def create_instrument(
    instrument: InstrumentCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # 🔒 Protegido
):
    return instrument_service.create_instrument_service(db, instrument)


@router.get("/", response_model=List[InstrumentResponse])
def list_instruments(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # 🔒 Protegido
):
    return instrument_service.list_instruments_service(db)


@router.get("/{instrument_id}", response_model=InstrumentResponse)
def get_instrument(
    instrument_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # 🔒 Protegido
):
    db_instrument = instrument_service.get_instrument_service(db, instrument_id)
    if not db_instrument:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instrument not found")
    return db_instrument


@router.put("/{instrument_id}", response_model=InstrumentResponse)
def update_instrument(
    instrument_id: int,
    instrument: InstrumentUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # 🔒 Protegido
):
    db_instrument = instrument_service.update_instrument_service(db, instrument_id, instrument)
    if not db_instrument:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instrument not found")
    return db_instrument


@router.delete("/{instrument_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_instrument(
    instrument_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # 🔒 Protegido
):
    deleted = instrument_service.delete_instrument_service(db, instrument_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instrument not found")
    return {"detail": "Instrument deleted successfully"}
