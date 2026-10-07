from flask_app.config.mysqlconnection import MySQLConnection

class Tarea:

    @classmethod
    def crear(cls, datos):
        query = """
        INSERT INTO tareas
        (titulo, prioridad, fecha_limite, descripcion, usuario_id, categoria_id)
        VALUES
        (%(titulo)s, %(prioridad)s, %(fecha_limite)s, %(descripcion)s,
         %(usuario_id)s, %(categoria_id)s)
        """
        return MySQLConnection("tasktrack").query_db(query, datos)

    @classmethod
    def listar_usuario(cls, usuario_id, estado=None, buscar=None):
        query = """
        SELECT tareas.*, categorias.nombre AS categoria
        FROM tareas
        JOIN categorias ON tareas.categoria_id = categorias.id
        WHERE tareas.usuario_id = %(usuario_id)s
        """
        datos = {"usuario_id": usuario_id}

        if estado:
            query += " AND tareas.estado = %(estado)s"
            datos["estado"] = estado

        if buscar:
            query += " AND tareas.titulo LIKE %(buscar)s"
            datos["buscar"] = "%" + buscar + "%"

        query += " ORDER BY tareas.fecha_limite ASC"

        return MySQLConnection("tasktrack").query_db(query, datos)

    @classmethod
    def buscar(cls, id, usuario_id):
        query = """
        SELECT tareas.*, categorias.nombre AS categoria
        FROM tareas
        JOIN categorias ON tareas.categoria_id = categorias.id
        WHERE tareas.id = %(id)s AND tareas.usuario_id = %(usuario_id)s
        """
        resultado = MySQLConnection("tasktrack").query_db(
            query, {"id": id, "usuario_id": usuario_id}
        )
        return resultado[0] if resultado else None

    @classmethod
    def editar(cls, datos):
        query = """
        UPDATE tareas
        SET titulo = %(titulo)s,
            categoria_id = %(categoria_id)s,
            prioridad = %(prioridad)s,
            fecha_limite = %(fecha_limite)s,
            descripcion = %(descripcion)s,
            estado = %(estado)s
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s
        """
        return MySQLConnection("tasktrack").query_db(query, datos)

    @classmethod
    def eliminar(cls, id, usuario_id):
        query = """
        DELETE FROM tareas
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s
        """
        return MySQLConnection("tasktrack").query_db(
            query, {"id": id, "usuario_id": usuario_id}
        )

    @classmethod
    def completar(cls, id, usuario_id):
        query = """
        UPDATE tareas
        SET estado = 'Completada'
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s
        """
        return MySQLConnection("tasktrack").query_db(
            query, {"id": id, "usuario_id": usuario_id}
        )

    @classmethod
    def contar_estados(cls, usuario_id):
        query = """
        SELECT estado, COUNT(*) AS cantidad
        FROM tareas
        WHERE usuario_id = %(usuario_id)s
        GROUP BY estado
        """
        return MySQLConnection("tasktrack").query_db(query, {"usuario_id": usuario_id})

    @classmethod
    def comentarios(cls, tarea_id):
        query = """
        SELECT comentarios.*, usuarios.nombre, usuarios.apellido
        FROM comentarios
        JOIN usuarios ON comentarios.usuario_id = usuarios.id
        WHERE comentarios.tarea_id = %(tarea_id)s
        ORDER BY comentarios.created_at ASC
        """
        return MySQLConnection("tasktrack").query_db(query, {"tarea_id": tarea_id})

    @classmethod
    def agregar_comentario(cls, datos):
        query = """
        INSERT INTO comentarios (comentario, usuario_id, tarea_id)
        VALUES (%(comentario)s, %(usuario_id)s, %(tarea_id)s)
        """
        return MySQLConnection("tasktrack").query_db(query, datos)
