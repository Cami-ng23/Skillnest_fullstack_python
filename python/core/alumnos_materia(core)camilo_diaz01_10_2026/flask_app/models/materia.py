from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.alumno import Alumno


class Materia:
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]
        self.alumnos = []

    @classmethod
    def listar(cls):
        consulta = """
            SELECT id, nombre, created_at, updated_at
            FROM materias
            ORDER BY nombre;
        """

        filas = connectToMySQL("base_alumnos_materias").query_db(consulta)

        materias = []

        for materia in filas:
            materias.append(cls(materia))

        return materias

    @classmethod
    def crear(cls, datos):
        consulta = """
            INSERT INTO materias (nombre)
            VALUES (%(nombre)s);
        """

        return connectToMySQL("base_alumnos_materias").query_db(
            consulta, datos
        )

    @classmethod
    def obtener_materia_con_alumnos(cls, materia_id):
        consulta = """
            SELECT
                m.id AS materia_id,
                m.nombre AS materia_nombre,
                m.created_at AS materia_created_at,
                m.updated_at AS materia_updated_at,
                a.id AS alumno_id,
                a.nombre AS alumno_nombre,
                a.apellido AS alumno_apellido,
                a.edad AS alumno_edad,
                a.created_at AS alumno_created_at,
                a.updated_at AS alumno_updated_at
            FROM materias m
            LEFT JOIN alumnos a
                ON m.id = a.materia_id
            WHERE m.id = %(id)s;
        """

        datos = {"id": materia_id}

        filas = connectToMySQL("base_alumnos_materias").query_db(
            consulta, datos
        )

        if not filas:
            return None

        materia_data = {
            "id": filas[0]["materia_id"],
            "nombre": filas[0]["materia_nombre"],
            "created_at": filas[0]["materia_created_at"],
            "updated_at": filas[0]["materia_updated_at"]
        }

        materia = cls(materia_data)

        for registro in filas:
            if registro["alumno_id"] is not None:
                alumno_data = {
                    "id": registro["alumno_id"],
                    "nombre": registro["alumno_nombre"],
                    "apellido": registro["alumno_apellido"],
                    "edad": registro["alumno_edad"],
                    "created_at": registro["alumno_created_at"],
                    "updated_at": registro["alumno_updated_at"],
                    "materia_id": materia.id
                }

                materia.alumnos.append(Alumno(alumno_data))

        return materia
