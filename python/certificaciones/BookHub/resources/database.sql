-- =====================================================
-- BookHub - Script de base de datos (MySQL 8 / MariaDB)
-- Uso:  mysql -u root -p < resources/database.sql
-- =====================================================
SET NAMES utf8mb4;
DROP DATABASE IF EXISTS bookhub;
CREATE DATABASE bookhub CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bookhub;

CREATE TABLE usuario (
    id          INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre      VARCHAR(50)  NOT NULL,
    apellido    VARCHAR(50)  NOT NULL,
    email       VARCHAR(120) NOT NULL,
    password    VARCHAR(255) NOT NULL,          -- hash Bcrypt, nunca texto plano
    created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_usuario_email (email)
) ENGINE=InnoDB;

CREATE TABLE libro (
    id                 INT UNSIGNED NOT NULL AUTO_INCREMENT,
    titulo             VARCHAR(150) NOT NULL,
    autor              VARCHAR(100) NOT NULL,
    genero             VARCHAR(50)  NOT NULL,
    fecha_publicacion  DATE         NOT NULL,
    descripcion        TEXT         NOT NULL,
    usuario_id         INT UNSIGNED NOT NULL,
    created_at         TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    CONSTRAINT fk_libro_usuario FOREIGN KEY (usuario_id)
        REFERENCES usuario (id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE favorito (
    id          INT UNSIGNED NOT NULL AUTO_INCREMENT,
    usuario_id  INT UNSIGNED NOT NULL,
    libro_id    INT UNSIGNED NOT NULL,
    created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_favorito_usuario_libro (usuario_id, libro_id),   -- evita favoritos duplicados
    CONSTRAINT fk_favorito_usuario FOREIGN KEY (usuario_id) REFERENCES usuario (id) ON DELETE CASCADE,
    CONSTRAINT fk_favorito_libro   FOREIGN KEY (libro_id)   REFERENCES libro (id)   ON DELETE CASCADE
) ENGINE=InnoDB;

-- ---------------- Datos de prueba (contraseña de todos: Test1234) ----------------
INSERT INTO usuario (nombre, apellido, email, password) VALUES
('Ana',    'Torres',  'ana@bookhub.com',    '$2b$12$8QrfgyYn3pDjaH2DrJxdsezIRJUjFQSP36l4xO5n./6FIPHjelNqu'),
('Carlos', 'Pérez',   'carlos@bookhub.com', '$2b$12$8QrfgyYn3pDjaH2DrJxdsezIRJUjFQSP36l4xO5n./6FIPHjelNqu'),
('Laura',  'Gómez',   'laura@bookhub.com',  '$2b$12$8QrfgyYn3pDjaH2DrJxdsezIRJUjFQSP36l4xO5n./6FIPHjelNqu'),
('Miguel', 'Ruiz',    'miguel@bookhub.com', '$2b$12$8QrfgyYn3pDjaH2DrJxdsezIRJUjFQSP36l4xO5n./6FIPHjelNqu'),
('Sofía',  'Méndez',  'sofia@bookhub.com',  '$2b$12$8QrfgyYn3pDjaH2DrJxdsezIRJUjFQSP36l4xO5n./6FIPHjelNqu'),
('Daniel', 'Castro',  'daniel@bookhub.com', '$2b$12$8QrfgyYn3pDjaH2DrJxdsezIRJUjFQSP36l4xO5n./6FIPHjelNqu');

INSERT INTO libro (titulo, autor, genero, fecha_publicacion, descripcion, usuario_id) VALUES
('Cien años de soledad',   'Gabriel García Márquez', 'Novela',              '2024-05-10', 'Una obra maestra del realismo mágico que narra la historia de la familia Buendía a lo largo de siete generaciones.', 1),
('El principito',          'Antoine de Saint-Exupéry','Fábula',             '2024-06-21', 'Un piloto varado en el desierto conoce a un pequeño príncipe que viaja de planeta en planeta.', 1),
('1984',                   'George Orwell',          'Ciencia Ficción',     '2024-07-15', 'Una distopía sobre un régimen totalitario que vigila y controla todos los aspectos de la vida.', 1),
('Orgullo y prejuicio',    'Jane Austen',            'Romance',             '2024-08-02', 'La historia de Elizabeth Bennet y el señor Darcy en la Inglaterra rural del siglo XIX.', 1),
('Dune',                   'Frank Herbert',          'Ciencia Ficción',     '2024-04-12', 'En el desértico planeta Arrakis se disputa la especia más valiosa del universo.', 2),
('Hábitos atómicos',       'James Clear',            'Desarrollo Personal', '2024-06-01', 'Un método práctico para crear buenos hábitos y eliminar los malos mediante pequeños cambios.', 3),
('El alquimista',          'Paulo Coelho',           'Novela',              '2024-06-18', 'Un joven pastor andaluz viaja en busca de un tesoro y descubre su leyenda personal.', 4);

INSERT INTO favorito (usuario_id, libro_id) VALUES
(1,5),(1,6),(1,7),(1,3),
(2,1),(3,1),(4,1),(5,1),(6,1),
(2,2),(3,3),(4,5),(5,6),(6,7);
