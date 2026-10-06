# BookHub

Aplicación web para registrar, consultar y administrar libros. El proyecto está desarrollado con Flask, MySQL, PyMySQL, Jinja2, Bootstrap y Bcrypt.

## Tecnologías

- Python
- Flask
- MySQL
- PyMySQL
- Jinja2
- Bootstrap 5
- Flask-Bcrypt

## Estructura

```text
BookHub/
├── app.py
├── database.py
├── requirements.txt
├── .env.example
├── controllers/
│   ├── auth_controller.py
│   ├── libro_controller.py
│   └── favorito_controller.py
├── models/
│   ├── usuario.py
│   ├── libro.py
│   └── favorito.py
├── templates/
├── static/
│   └── css/
└── resources/
    ├── database.sql
    └── BookHub_ERD.png
```

Los controladores contienen las rutas y la lógica de la aplicación, los modelos contienen las clases y validaciones principales, y `database.py` contiene la conexión y consultas básicas a MySQL.

## Instalación

1. Crear un entorno virtual:

```bash
python -m venv venv
```

2. Activarlo en Windows:

```bash
venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Crear la base de datos ejecutando `resources/database.sql` en MySQL.

5. Crear un archivo `.env` a partir de `.env.example` y completar los datos de conexión.

6. Ejecutar:

```bash
python app.py
```

Luego abrir `http://localhost:5000/`.

## Funcionalidades

- Registro e inicio de sesión.
- Contraseñas protegidas con Bcrypt.
- Sesiones de usuario.
- Crear, consultar, editar y eliminar libros.
- Libros de la comunidad.
- Favoritos.
- Detalle de cada libro y usuarios que lo marcaron como favorito.
- Validaciones en backend y mensajes flash.
- Control de permisos: cada usuario solamente puede modificar o eliminar sus propios libros.
