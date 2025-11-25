from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    gender: str
    class_: str

class CharacterCreate(CharacterBase):
    pass

class CharacterUpdate(CharacterBase):
    pass

class CharacterOut(CharacterBase):
    id: int
    class Config:
        orm_mode = True
