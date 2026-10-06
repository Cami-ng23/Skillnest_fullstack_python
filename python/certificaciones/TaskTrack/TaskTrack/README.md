# TaskTrack

Proyecto Flask + MySQL + MVC para la simulación de examen.

## 1. Crear la base de datos

Abre MySQL Workbench y ejecuta:

database.sql

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 3. Revisar .env

Configura usuario, contraseña y nombre de la base de datos.

## 4. Ejecutar

```bash
python server.py
```

Luego entra a:

http://localhost:5000/

## Funciones incluidas

- Registro
- Login
- Bcrypt
- Sesiones
- Crear tareas
- Ver detalle
- Editar tareas
- Eliminar tareas
- Categorías
- Estados
- Buscar tareas
- Filtrar por estado
- Marcar como completada
- Comentarios
- Permisos por usuario
- Validaciones
