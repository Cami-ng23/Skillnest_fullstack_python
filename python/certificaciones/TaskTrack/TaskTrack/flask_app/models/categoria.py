from flask_app.config.mysqlconnection import MySQLConnection

class Categoria:

    @classmethod
    def crear(cls, datos):
        query = """
        INSERT INTO categorias (nombre, usuario_id)
        VALUES (%(nombre)s, %(usuario_id)s)
        """
        return MySQLConnection("tasktrack").query_db(query, datos)

    @classmethod
    def listar_usuario(cls, usuario_id):
        query = """
        SELECT * FROM categorias
        WHERE usuario_id = %(usuario_id)s
        ORDER BY nombre
        """
        return MySQLConnection("tasktrack").query_db(query, {"usuario_id": usuario_id})

    @classmethod
    def buscar(cls, id, usuario_id):
        query = """
        SELECT * FROM categorias
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s
        """
        resultado = MySQLConnection("tasktrack").query_db(
            query, {"id": id, "usuario_id": usuario_id}
        )
        return resultado[0] if resultado else None

    @classmethod
    def editar(cls, datos):
        query = """
        UPDATE categorias
        SET nombre = %(nombre)s
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s
        """
        return MySQLConnection("tasktrack").query_db(query, datos)

    @classmethod
    def eliminar(cls, id, usuario_id):
        query = """
        DELETE FROM categorias
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s
        """
        return MySQLConnection("tasktrack").query_db(
            query, {"id": id, "usuario_id": usuario_id}
        )
