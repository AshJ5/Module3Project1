from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

# Association table for class-weapon relationship
class_valid_weps = Table(
    'class_valid_weps',
    Base.metadata,
    Column('class_id', Integer, ForeignKey('classes.id'), primary_key=True),
    Column('weapon_id', Integer, ForeignKey('weapons.id'), primary_key=True)
)


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    icon_path = Column(String(255))

    # Relationship to weapons through association table
    valid_weapons = relationship(
        "Weapon",
        secondary=class_valid_weps,
        back_populates="valid_for_classes"
    )
    characters = relationship("Character", back_populates="character_class")


class Weapon(Base):
    __tablename__ = "weapons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    damage_type = Column(String(20))
    sprite_image = Column(String(255))

    # Relationship to classes through association table
    valid_for_classes = relationship(
        "Class",
        secondary=class_valid_weps,
        back_populates="valid_weapons"
    )
    characters = relationship("Character", back_populates="equipped_weapon")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    class_id = Column(Integer, ForeignKey('classes.id'))
    equipped_weapon_id = Column(Integer, ForeignKey('weapons.id'))

    # Relationships
    character_class = relationship("Class", back_populates="characters")
    equipped_weapon = relationship("Weapon", back_populates="characters")
