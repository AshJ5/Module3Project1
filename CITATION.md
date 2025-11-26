# Citations
---

### SCHEMAS GENERATION:

- Gemini. (2025, November 25). Generation of schema for project [Conversation with Gemini]. Google. https://gemini.google.com/share/1620baedf81f

---
Here's the project summary in APA format:

---

**Software Development Session: Character Creation System for Adventure Game**

*Project Overview*

A full-stack web application featuring an animated character creation interface for an adventure-themed game. The system comprises a React-based frontend with Vite build tooling and a FastAPI backend with SQLite database integration (November 26, 2025).

*Technical Implementation*

The frontend architecture employs three distinct pages: an animated introduction sequence, a title screen, and an interactive character creation form. Navigation between pages utilizes React state management, while dynamic asset loading leverages Vite's `import.meta.glob()` functionality for efficient image bundling. User interface components include class and weapon selection dropdowns with real-time image preview capabilities and form validation.

The backend implements a RESTful API using FastAPI (Version 0.109.0) with SQLAlchemy ORM (Version 2.0.23) for database abstraction. The data model encompasses three primary entities—Class, Weapon, and Character—with a many-to-many relationship between classes and weapons implemented through a junction table. Pydantic schemas (Version 2.5.0) provide request/response validation, while Cross-Origin Resource Sharing (CORS) middleware enables secure frontend-backend communication.

*Database Schema*

The SQLite database contains four character classes (Deli Worker, Waffle House Cook, Milkman, and Retail Worker), each associated with two unique weapons. Current weapon inventory includes: Gouda Cheese Block and Sausage Sword (Deli Worker); Skillet and Waffle House Fist Style (Waffle House Cook); Milk Bottle and Creepy Smile (Milkman); Retail Pole Hook and Shopping Cart (Retail Worker).

*Development Environment Configuration*

The project utilizes Python 3.12.8 within an isolated virtual environment, necessitated by Pydantic v2 compatibility constraints with Python 3.14. The backend directory structure follows modular design principles with separate subdirectories for application logic (`app/`), utility scripts (`scripts/`), and SQL schemas (`sql_schemas/`).

*Deployment Instructions*

Backend server: Execute `winpty venv/Scripts/python.exe -m uvicorn app.main:app --reload --port 8000` from the backend directory.

Frontend development server: Execute `npm run dev` from the adventure directory.

The application runs on localhost with the backend accessible at port 8000 and frontend at port 5174, with full API documentation available via Swagger UI at `http://localhost:8000/docs`.

---