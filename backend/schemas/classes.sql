CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    icon_path VARCHAR(255) -- e.g., '/assets/deli/char1.png', '/assets/wafflehouse/char2.png', '/assets/milkman/char3.png', '/assets/retail/char4.png'
);