CREATE DATABASE usuarios_db;
USE usuarios_db;

CREATE TABLE tipo_usuario (
    id_tipo INT AUTO_INCREMENT PRIMARY KEY,
    nombre_tipo VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO tipo_usuario (nombre_tipo)
VALUES
('ADMIN'),
('USER');

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    tipo_usuario INT NOT NULL,

    -- Campos de auditoría
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE,

    CONSTRAINT fk_tipo_usuario
        FOREIGN KEY (tipo_usuario)
        REFERENCES tipo_usuario(id_tipo)
);


INSERT INTO usuarios
(usuario, password, tipo_usuario)
VALUES
('Carlos', '1234', 1);


INSERT INTO usuarios
(usuario, password, tipo_usuario)
VALUES
('Juan', '1234', 2);