CREATE TABLE characters (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    class_id INTEGER,
    equipped_weapon_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES classes (id),
    FOREIGN KEY (equipped_weapon_id) REFERENCES weapons (id)
);