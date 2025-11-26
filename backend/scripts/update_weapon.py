from app.models import Weapon
from app.database import SessionLocal
import sys
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.insert(0, str(Path(__file__).parent.parent))


db = SessionLocal()
weapon = db.query(Weapon).filter(Weapon.id == 5).first()
weapon.name = 'Retail Pole Hook'
db.commit()
print('Updated weapon name to Retail Pole Hook')
db.close()
