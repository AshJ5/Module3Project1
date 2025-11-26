from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base, get_db
from app.models import Character, Class, Weapon
from app.schemas import (
    CharacterCreate, CharacterUpdate, CharacterOut, CharacterDetailed,
    ClassOut, WeaponOut
)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Adventure API")

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
                   "http://localhost:3000"],  # Vite default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Class Endpoints =====


@app.get("/api/classes", response_model=List[ClassOut])
def get_classes(db: Session = Depends(get_db)):
    """Get all available classes"""
    return db.query(Class).all()


@app.get("/api/classes/{class_id}", response_model=ClassOut)
def get_class(class_id: int, db: Session = Depends(get_db)):
    """Get a specific class by ID"""
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_obj


@app.get("/api/classes/{class_id}/weapons", response_model=List[WeaponOut])
def get_class_weapons(class_id: int, db: Session = Depends(get_db)):
    """Get all valid weapons for a specific class"""
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_obj.valid_weapons

# ===== Weapon Endpoints =====


@app.get("/api/weapons", response_model=List[WeaponOut])
def get_weapons(db: Session = Depends(get_db)):
    """Get all weapons"""
    return db.query(Weapon).all()


@app.get("/api/weapons/{weapon_id}", response_model=WeaponOut)
def get_weapon(weapon_id: int, db: Session = Depends(get_db)):
    """Get a specific weapon by ID"""
    weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon

# ===== Character Endpoints =====


@app.post("/api/characters", response_model=CharacterOut)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    """Create a new character"""
    # Validate class exists
    class_obj = db.query(Class).filter(Class.id == character.class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")

    # Validate weapon exists and is valid for the class
    weapon = db.query(Weapon).filter(
        Weapon.id == character.equipped_weapon_id).first()
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")

    if weapon not in class_obj.valid_weapons:
        raise HTTPException(
            status_code=400, detail="Weapon is not valid for this class")

    # Create character
    db_character = Character(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


@app.get("/api/characters", response_model=List[CharacterOut])
def list_characters(db: Session = Depends(get_db)):
    """Get all characters"""
    return db.query(Character).all()


@app.get("/api/characters/{character_id}", response_model=CharacterDetailed)
def get_character(character_id: int, db: Session = Depends(get_db)):
    """Get a specific character with full details"""
    character = db.query(Character).filter(
        Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@app.put("/api/characters/{character_id}", response_model=CharacterOut)
def update_character(character_id: int, update: CharacterUpdate, db: Session = Depends(get_db)):
    """Update a character"""
    character = db.query(Character).filter(
        Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    # Update only provided fields
    update_data = update.model_dump(exclude_unset=True)

    # Validate weapon/class combination if both are being updated
    if "class_id" in update_data or "equipped_weapon_id" in update_data:
        class_id = update_data.get("class_id", character.class_id)
        weapon_id = update_data.get(
            "equipped_weapon_id", character.equipped_weapon_id)

        class_obj = db.query(Class).filter(Class.id == class_id).first()
        weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()

        if weapon not in class_obj.valid_weapons:
            raise HTTPException(
                status_code=400, detail="Weapon is not valid for this class")

    for key, value in update_data.items():
        setattr(character, key, value)

    db.commit()
    db.refresh(character)
    return character


@app.delete("/api/characters/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_db)):
    """Delete a character"""
    character = db.query(Character).filter(
        Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(character)
    db.commit()
    return {"message": "Character deleted successfully"}


@app.get("/")
def root():
    return {"message": "Adventure API is running"}
