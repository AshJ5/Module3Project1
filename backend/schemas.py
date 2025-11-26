from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

# Class Schemas


class ClassBase(BaseModel):
    name: str
    description: Optional[str] = None
    icon_path: Optional[str] = None


class ClassOut(ClassBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Weapon Schemas


class WeaponBase(BaseModel):
    name: str
    damage_type: Optional[str] = None
    sprite_image: Optional[str] = None


class WeaponOut(WeaponBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Character Schemas


class CharacterBase(BaseModel):
    name: str = Field(..., max_length=50)
    class_id: int
    equipped_weapon_id: int


class CharacterCreate(CharacterBase):
    pass


class CharacterUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    class_id: Optional[int] = None
    equipped_weapon_id: Optional[int] = None


class CharacterOut(CharacterBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class CharacterDetailed(BaseModel):
    id: int
    name: str
    character_class: ClassOut
    equipped_weapon: WeaponOut
    model_config = ConfigDict(from_attributes=True)
