# Alumnos y Materias

Proyecto Flask + MySQL + PyMySQL + Jinja2 + Bootstrap.

## Estructura

- `flask_app/` contiene la aplicación.
- `models/` contiene las clases Materia y Alumno.
- `controllers/` contiene las rutas.
- `templates/` contiene las páginas HTML.
- `static/` contiene los estilos.
- `bd/` contiene el SQL.

## Ejecutar

1. Crear la base de datos usando:
   `flask_app/bd/base_alumnos_materias.sql`

2. Instalar dependencias:
   `pip install flask pymysql`

3. Ejecutar:
   `python server.py`

4. Abrir:
   `http://127.0.0.1:5000`
