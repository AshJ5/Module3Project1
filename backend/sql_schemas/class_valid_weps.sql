CREATE TABLE class_valid_weps (
    class_id INTEGER,
    weapon_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES classes (id),
    FOREIGN KEY (weapon_id) REFERENCES weapons (id),
    PRIMARY KEY (class_id, weapon_id) -- Prevents duplicate rules
);