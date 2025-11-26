# Backend API Setup Instructions

## Prerequisites
- Python 3.8+
- pip

## Installation

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Database Setup

1. The application will create an SQLite database automatically on first run

2. Run the SQL scripts to populate the database:
   - First, start the server (see below)
   - Then manually run the SQL insert scripts in your database tool, or use Python:

```python
from database import engine
from sqlalchemy import text

with engine.connect() as conn:
    # Read and execute each SQL file
    with open('schemas/classes_insert.sql', 'r') as f:
        conn.execute(text(f.read()))
    with open('schemas/weapons_insert.sql', 'r') as f:
        conn.execute(text(f.read()))
    with open('schemas/class_valid_weps_insert.sql', 'r') as f:
        conn.execute(text(f.read()))
    conn.commit()
```

## Running the API

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

API Documentation (Swagger UI): `http://localhost:8000/docs`

## API Endpoints

### Classes
- `GET /api/classes` - Get all classes
- `GET /api/classes/{class_id}` - Get a specific class
- `GET /api/classes/{class_id}/weapons` - Get valid weapons for a class

### Weapons
- `GET /api/weapons` - Get all weapons
- `GET /api/weapons/{weapon_id}` - Get a specific weapon

### Characters
- `POST /api/characters` - Create a new character
- `GET /api/characters` - Get all characters
- `GET /api/characters/{character_id}` - Get a specific character
- `PUT /api/characters/{character_id}` - Update a character
- `DELETE /api/characters/{character_id}` - Delete a character

## Environment Variables

Create a `.env` file in the backend directory (optional):
```
DATABASE_URL=sqlite:///./adventure.db
```

For PostgreSQL:
```
DATABASE_URL=postgresql://user:password@localhost/adventure_db
```

## Frontend Connection

The frontend is already configured to connect to `http://localhost:8000/api`.
Make sure both the backend server and frontend dev server are running simultaneously.
