from flask_app.config.mysqlconnection import conectar_mysql
from flask_app.models.estudiante import Estudiante


class Curso:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.estudiantes = []

    @classmethod
    def get_all(cls):
        sentencia = "SELECT id, nombre, created_at, updated_at FROM cursos ORDER BY nombre;"
        filas_bd = conectar_mysql("esquema_estudiantes_cursos").ejecutar_consulta(sentencia)

        lista_cursos = []
        if filas_bd:
            for registro_curso in filas_bd:
                lista_cursos.append(cls(registro_curso))
        return lista_cursos

    @classmethod
    def save(cls, datos_curso):
        sentencia = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return conectar_mysql("esquema_estudiantes_cursos").ejecutar_consulta(sentencia, datos_curso)

    @classmethod
    def get_curso_con_estudiantes(cls, id_curso):
        sentencia = """
            SELECT
                c.id AS curso_id, c.nombre AS curso_nombre,
                c.created_at AS curso_created_at, c.updated_at AS curso_updated_at,
                e.id AS estudiante_id, e.nombre AS estudiante_nombre,
                e.apellido AS estudiante_apellido, e.edad AS estudiante_edad,
                e.created_at AS estudiante_created_at, e.updated_at AS estudiante_updated_at
            FROM cursos c
            LEFT JOIN estudiantes e ON c.id = e.curso_id
            WHERE c.id = %(id)s;
        """
        parametros = {"id": id_curso}
        filas_detalle = conectar_mysql("esquema_estudiantes_cursos").ejecutar_consulta(sentencia, parametros)

        if not filas_detalle:
            return None

        datos_curso = {
            "id": filas_detalle[0]["curso_id"],
            "nombre": filas_detalle[0]["curso_nombre"],
            "created_at": filas_detalle[0]["curso_created_at"],
            "updated_at": filas_detalle[0]["curso_updated_at"]
        }
        curso_actual = cls(datos_curso)

        for registro in filas_detalle:
            if registro["estudiante_id"] is not None:
                datos_estudiante = {
                    "id": registro["estudiante_id"],
                    "nombre": registro["estudiante_nombre"],
                    "apellido": registro["estudiante_apellido"],
                    "edad": registro["estudiante_edad"],
                    "created_at": registro["estudiante_created_at"],
                    "updated_at": registro["estudiante_updated_at"],
                    "curso_id": curso_actual.id
                }
                curso_actual.estudiantes.append(Estudiante(datos_estudiante))
        return curso_actual
