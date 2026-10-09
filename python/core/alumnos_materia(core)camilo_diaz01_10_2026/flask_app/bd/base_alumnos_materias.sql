CREATE DATABASE IF NOT EXISTS base_alumnos_materias;

USE base_alumnos_materias;

CREATE TABLE IF NOT EXISTS materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    edad INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    materia_id INT NOT NULL,

    CONSTRAINT fk_alumnos_materia
        FOREIGN KEY (materia_id)
        REFERENCES materias(id)
);

INSERT INTO materias (nombre)
VALUES
("Flask"),
("JavaScript"),
("Python Web"),
("Desarrollo Web");

INSERT INTO alumnos (nombre, apellido, edad, materia_id)
VALUES
("Camila", "Rojas", 24, 1),
("Diego", "Muñoz", 23, 1),
("Matías", "Vega", 26, 1),
("Nicolás", "Pérez", 25, 1),
("Sofía", "Torres", 22, 2),
("Benjamín", "Soto", 21, 3);
