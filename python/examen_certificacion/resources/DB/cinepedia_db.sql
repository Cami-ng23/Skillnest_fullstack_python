Create database cinepedia;
use cinepedia;

create table usuarios (
id INT PRIMARY KEY auto_increment,
apellido varchar(30) not null,
email varchar(100) not null,
password varchar(255) not null,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

create table peliculas(
id INT PRIMARY KEY auto_increment,
nombre_pelicula varchar(100) unique not null,
director_pelicula varchar(50) not null,
fecha_estreno time not null,
sinopsis varchar(300) not null
);

create table comentarios(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre_comentario varchar(50)  not null,
descripcion_comentario varchar (200)
);

INSERT INTO peliculas (nombre_pelicula, director_pelicula, fecha_estreno, sinopsis) VALUES
("batman", "felipe muñoz", 10-09-2025, "una pelicula de superheroe que combate los criminales de la ciudad en la noche"); 
