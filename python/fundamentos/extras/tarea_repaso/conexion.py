import pymysql

class Conexion:

    def conectar(self):

        conexion = pymysql.connect(

            host="localhost",
            user="root",
            password="1234",
            database="usuarios_db"
        )

        return conexion

    def cerrar(self,conexion):
        conexion.close()