from flask_app.config.mysqlconnection import connectToMySQL


class Alumno:
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.edad = datos["edad"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]
        self.materia_id = datos["materia_id"]

    @classmethod
    def crear(cls, datos):
        consulta = """
            INSERT INTO alumnos
            (nombre, apellido, edad, materia_id)
            VALUES
            (%(nombre)s, %(apellido)s, %(edad)s, %(materia_id)s);
        """

        return connectToMySQL("base_alumnos_materias").query_db(
            consulta, datos
        )
