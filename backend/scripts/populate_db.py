"""
Script to populate the database with initial data for classes, weapons, and their relationships
"""
from app.models import Class, Weapon, class_valid_weps
from app.database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
import sys
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.insert(0, str(Path(__file__).parent.parent))


# Create all tables
Base.metadata.create_all(bind=engine)


def populate_database():
    db = SessionLocal()

    try:
        # Check if data already exists
        if db.query(Class).first() is not None:
            print("Database already populated!")
            return

        # Create classes
        classes_data = [
            {
                "id": 1,
                "name": "Deli Worker",
                "description": "A master of slicing and serving",
                "icon_path": "/assets/deli/char1.png"
            },
            {
                "id": 2,
                "name": "Waffle House Cook",
                "description": "Expert at flipping and grilling",
                "icon_path": "/assets/wafflehouse/char2.png"
            },
            {
                "id": 3,
                "name": "Milkman",
                "description": "Delivers dairy with precision",
                "icon_path": "/assets/milkman/char3.png"
            },
            {
                "id": 4,
                "name": "Retail Worker",
                "description": "Skilled in customer service",
                "icon_path": "/assets/retail/char4.png"
            }
        ]

        classes = []
        for class_data in classes_data:
            class_obj = Class(**class_data)
            db.add(class_obj)
            classes.append(class_obj)

        db.commit()
        print("✓ Classes added successfully")

        # Create weapons
        weapons_data = [
            {
                "id": 1,
                "name": "Gouda Cheese Block",
                "damage_type": "Slashing",
                "sprite_image": "/assets/deli/wep1.png"
            },
            {
                "id": 2,
                "name": "Sausage Sword",
                "damage_type": "Piercing",
                "sprite_image": "/assets/deli/wep2.png"
            },
            {
                "id": 3,
                "name": "Milk Bottle",
                "damage_type": "Blunt",
                "sprite_image": "/assets/milkman/wep3.png"
            },
            {
                "id": 4,
                "name": "Creepy Smile",
                "damage_type": "Blunt",
                "sprite_image": "/assets/milkman/wep4.png"
            },
            {
                "id": 5,
                "name": "Retail Pole Hook",
                "damage_type": "Ranged",
                "sprite_image": "/assets/retail/wep5.png"
            },
            {
                "id": 6,
                "name": "Shopping Cart",
                "damage_type": "Blunt",
                "sprite_image": "/assets/retail/wep6.png"
            },
            {
                "id": 7,
                "name": "Skillet",
                "damage_type": "Slashing",
                "sprite_image": "/assets/wafflehouse/wep7.png"
            },
            {
                "id": 8,
                "name": "Waffle House Fist Style",
                "damage_type": "Blunt",
                "sprite_image": "/assets/wafflehouse/wep8.png"
            }
        ]

        weapons = []
        for weapon_data in weapons_data:
            weapon_obj = Weapon(**weapon_data)
            db.add(weapon_obj)
            weapons.append(weapon_obj)

        db.commit()
        print("✓ Weapons added successfully")

        # Create class-weapon relationships
        class_weapon_mapping = [
            (1, 1),  # Deli Worker - Meat Slicer
            (1, 2),  # Deli Worker - Deli Knife
            (2, 7),  # Waffle House Cook - Spatula
            (2, 8),  # Waffle House Cook - Waffle Iron
            (3, 3),  # Milkman - Milk Bottle
            (3, 4),  # Milkman - Delivery Crate
            (4, 5),  # Retail Worker - Price Gun
            (4, 6),  # Retail Worker - Shopping Cart
        ]

        for class_id, weapon_id in class_weapon_mapping:
            stmt = class_valid_weps.insert().values(
                class_id=class_id,
                weapon_id=weapon_id
            )
            db.execute(stmt)

        db.commit()
        print("✓ Class-weapon relationships added successfully")

        print("\n✅ Database populated successfully!")
        print(f"   - {len(classes)} classes")
        print(f"   - {len(weapons)} weapons")
        print(f"   - {len(class_weapon_mapping)} class-weapon combinations")

    except Exception as e:
        print(f"❌ Error populating database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    populate_database()
