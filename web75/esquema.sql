DROP TABLE IF EXISTS personal;
DROP TABLE IF EXISTS contacto;

CREATE TABLE personal{
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    foto TEXT,
    tarjeta TEXT NOT NULL
};

CREATE TABLE contacto{
    tel TEXT,
    dir TEXT,
    mapa TEXT
};
