CREATE DATABASE biblioteca;
USE biblioteca;

-- Tabla direcciones
CREATE TABLE direcciones (
    id_direccion INT PRIMARY KEY AUTO_INCREMENT,
    comuna VARCHAR(100),
    calle VARCHAR(100),
    numero_residencia VARCHAR(10),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0,
);

-- Tabla usuarios
CREATE TABLE usuarios (
    id_usuarios INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(45),
    email VARCHAR(150),
    id_direccion INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0,

    FOREIGN KEY (id_direccion)
    REFERENCES direcciones(id_direccion)
);

-- Tabla libros
CREATE TABLE libros (
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    autor VARCHAR(45),
    titulo VARCHAR(150),
    anio_publicacion DATETIME,
    disponible TINYINT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0,
);

-- Tabla prestamos
CREATE TABLE prestamos (
    id_prestamo INT PRIMARY KEY AUTO_INCREMENT,
    fecha_prestamo DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0,
    id_usuarios INT,
    id_libro INT,

    FOREIGN KEY (id_usuarios)
    REFERENCES usuarios(id_usuarios),

    FOREIGN KEY (id_libro)
    REFERENCES libros(id_libro)
);

-- Tabla personas
CREATE TABLE personas (
    id_persona INT PRIMARY KEY AUTO_INCREMENT,
    rut VARCHAR(9),
    fecha_nac DATE,
    id_usuario INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0,

    FOREIGN KEY (id_usuario)
    REFERENCES usuarios(id_usuarios)
);
