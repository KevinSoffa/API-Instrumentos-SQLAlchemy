from sqlalchemy.orm import Session
from models.instrument_model import Instrument
from schema.instrument_schema import InstrumentCreate, InstrumentUpdate


def create_instrument(db: Session, instrument: InstrumentCreate):
    db_instrument = Instrument(**instrument.dict())
    db.add(db_instrument)
    db.commit()
    db.refresh(db_instrument)
    return db_instrument

def get_instruments(db: Session):
    return db.query(Instrument).all()

def get_instrument_by_id(db: Session, instrument_id: int):
    return db.query(Instrument).filter(Instrument.id == instrument_id).first()

def update_instrument(db: Session, instrument_id: int, instrument: InstrumentUpdate):
    db_instrument = get_instrument_by_id(db, instrument_id)
    if not db_instrument:
        return None
    for field, value in instrument.dict().items():
        setattr(db_instrument, field, value)
    db.commit()
    db.refresh(db_instrument)
    return db_instrument

def delete_instrument(db: Session, instrument_id: int):
    db_instrument = get_instrument_by_id(db, instrument_id)
    if db_instrument:
        db.delete(db_instrument)
        db.commit()
        return True
    return False
