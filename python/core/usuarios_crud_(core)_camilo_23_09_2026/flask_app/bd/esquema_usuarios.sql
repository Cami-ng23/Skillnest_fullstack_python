CREATE DATABASE IF NOT EXISTS esquema_usuarios;

USE esquema_usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nombre, apellido, email) VALUES
('Carlos', 'González', 'carlos@gmail.com'),
('Daniela', 'Rojas', 'daniela@gmail.com'),
('Matías', 'Soto', 'matias@gmail.com');
