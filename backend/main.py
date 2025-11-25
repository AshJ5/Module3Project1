from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Character
from schemas import CharacterCreate, CharacterUpdate, CharacterOut

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/characters", response_model=CharacterOut)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

@app.get("/characters", response_model=list[CharacterOut])
def list_characters(db: Session = Depends(get_db)):
    return db.query(Character).all()

@app.get("/characters/{character_id}", response_model=CharacterOut)
def get_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@app.put("/characters/{character_id}", response_model=CharacterOut)
def update_character(character_id: int, update: CharacterUpdate, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    for key, value in update.dict().items():
        setattr(character, key, value)
    db.commit()
    db.refresh(character)
    return character

@app.delete("/characters/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(character)
    db.commit()
    return {"message": "Character deleted"}
