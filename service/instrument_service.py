from sqlalchemy.orm import Session
from repository import instrument_repository
from schema.instrument_schema import InstrumentCreate, InstrumentUpdate


def create_instrument_service(db: Session, instrument: InstrumentCreate):
    return instrument_repository.create_instrument(db, instrument)

def list_instruments_service(db: Session):
    return instrument_repository.get_instruments(db)

def get_instrument_service(db: Session, instrument_id: int):
    return instrument_repository.get_instrument_by_id(db, instrument_id)

def update_instrument_service(db: Session, instrument_id: int, instrument: InstrumentUpdate):
    return instrument_repository.update_instrument(db, instrument_id, instrument)

def delete_instrument_service(db: Session, instrument_id: int):
    return instrument_repository.delete_instrument(db, instrument_id)
