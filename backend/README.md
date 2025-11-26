# Backend Structure

```
backend/
├── app/                    # Main application package
│   ├── __init__.py
│   ├── main.py            # FastAPI app and routes
│   ├── database/          # Database configuration
│   │   ├── __init__.py
│   │   └── database.py    # SQLAlchemy setup
│   ├── models/            # Database models
│   │   ├── __init__.py
│   │   └── models.py      # SQLAlchemy ORM models
│   └── schemas/           # Pydantic schemas
│       ├── __init__.py
│       └── schemas.py     # Request/response models
├── scripts/               # Utility scripts
│   ├── populate_db.py     # Database seeding
│   └── update_weapon.py   # Database update utilities
├── sql_schemas/           # SQL schema files
│   └── old_schemas/       # Legacy SQL files
├── adventure.db           # SQLite database file
├── requirements.txt       # Python dependencies
└── venv/                  # Virtual environment

```

## Running the Application

From the `backend` directory:

1. Activate virtual environment:
   ```bash
   . venv/Scripts/activate
   ```

2. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```
   
   Or run directly without activating venv (Windows Git Bash):
   ```bash
   winpty venv/Scripts/python.exe -m uvicorn app.main:app --reload
   ```

3. Access the API:
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs

## Scripts

Run scripts from the `backend` directory:

```bash
# Populate database with initial data
python scripts/populate_db.py

# Update weapon names
python scripts/update_weapon.py
```
