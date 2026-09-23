from flask_app.config.mysqlconnection import MySQLConnection


class Usuario:

    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @classmethod
    def get_all(cls):
        consulta = "SELECT * FROM usuarios;"
        resultados = MySQLConnection("esquema_usuarios").query_db(consulta)

        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @classmethod
    def get_by_id(cls, datos):
        consulta = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = MySQLConnection("esquema_usuarios").query_db(consulta, datos)

        if resultado:
            return cls(resultado[0])

        return None

    @classmethod
    def save(cls, datos):
        consulta = """
            INSERT INTO usuarios (nombre, apellido, email)
            VALUES (%(nombre)s, %(apellido)s, %(email)s);
        """
        return MySQLConnection("esquema_usuarios").query_db(consulta, datos)

    @classmethod
    def update(cls, datos):
        consulta = """
            UPDATE usuarios
            SET nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s
            WHERE id = %(id)s;
        """
        return MySQLConnection("esquema_usuarios").query_db(consulta, datos)

    @classmethod
    def delete(cls, datos):
        consulta = "DELETE FROM usuarios WHERE id = %(id)s;"
        return MySQLConnection("esquema_usuarios").query_db(consulta, datos)
