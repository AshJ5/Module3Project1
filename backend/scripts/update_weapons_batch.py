from app.models import Weapon
from app.database import SessionLocal
import sys
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.insert(0, str(Path(__file__).parent.parent))


db = SessionLocal()

# Update weapon names
updates = [
    (1, 'Gouda Cheese Block'),
    (2, 'Sausage Sword'),
    (7, 'Skillet'),
    (8, 'Waffle House Fist Style')
]

for weapon_id, new_name in updates:
    weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
    if weapon:
        weapon.name = new_name
        print(f'Updated weapon {weapon_id}: {new_name}')

db.commit()
print('\n✓ All weapon names updated successfully')
db.close()
