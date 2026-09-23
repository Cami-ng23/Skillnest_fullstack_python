# Usuarios CRUD - MVC

Esta asignación toma el CRUD de Usuarios y lo organiza usando el patrón MVC de Flask.

## Estructura

- `models`: trabaja con los datos y la base de datos.
- `controllers`: contiene las rutas de Flask.
- `templates`: contiene las páginas HTML.
- `config`: contiene la conexión a MySQL.
- `bd`: contiene el script SQL.
- `server.py`: inicia la aplicación.

## Para ejecutar

1. Ejecutar `flask_app/bd/esquema_usuarios.sql` en MySQL.
2. Revisar usuario y contraseña de MySQL en `flask_app/config/mysqlconnection.py`.
3. Instalar las dependencias con `pipenv install`.
4. Ejecutar `pipenv run python server.py`.
5. Entrar a `http://127.0.0.1:5000/usuarios`.
