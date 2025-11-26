CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    icon_path VARCHAR(255) -- e.g., '/assets/icons/classes/warrior.png'
);