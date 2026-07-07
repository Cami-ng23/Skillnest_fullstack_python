from conexion import Conexion


class Usuario:

    def __init__(self, id=None, usuario="", password="", tipo_usuario=None):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo_usuario = tipo_usuario

    def guardar(self):
        conexion = Conexion().conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuarios(usuario, password, tipo_usuario)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (
            self.usuario,
            self.password,
            self.tipo_usuario
        ))

        conexion.commit()
        conexion.close()

    def listar(self):
        conexion = Conexion().conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT u.id, u.usuario, t.nombre_tipo
        FROM usuarios u
        INNER JOIN tipo_usuario t ON u.tipo_usuario = t.id_tipo
        WHERE u.deleted = FALSE
        """

        cursor.execute(sql)
        datos = cursor.fetchall()

        conexion.close()
        return datos
    
    def buscar(self):

        conexion = Conexion().conectar()
        cursor = conexion.cursor()

        sql = "SELECT * FROM usuarios WHERE id=%s"

        cursor.execute(sql, (self.id,))
        dato = cursor.fetchone()
        conexion.close()
        return dato

    def modificar(self):

        conexion = Conexion().conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuarios
        SET usuario=%s,
            password=%s,
            tipo_usuario=%s
        WHERE id=%s
        """

        cursor.execute(sql, (
            self.usuario,
            self.password,
            self.tipo_usuario,
            self.id
        ))

        conexion.commit()
        conexion.close()

    def eliminar(self):

        conexion = Conexion().conectar()
        cursor = conexion.cursor()

        sql = "UPDATE usuarios SET deleted=TRUE WHERE id=%s"

        cursor.execute(sql, (self.id,))

        conexion.commit()
        conexion.close()

    def login(self):

        conexion = Conexion().conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT u.id, u.usuario, t.nombre_tipo
        FROM usuarios u
        INNER JOIN tipo_usuario t ON u.tipo_usuario = t.id_tipo
        WHERE u.usuario=%s
        AND u.password=%s
        AND u.deleted=FALSE
        """

        cursor.execute(sql, (self.usuario, self.password))
        resultado = cursor.fetchone()

        conexion.close()
        return resultado