import pymysql
import pymysql.cursors

class MySQLConnection:
    def __init__(self, nombre_bd):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234", 
            database=nombre_bd,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def ejecutar_consulta(self, sentencia, parametros=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sentencia, parametros or {})
                tipo_consulta = sentencia.strip().lower()

                if tipo_consulta.startswith("select"):
                    return cursor.fetchall()
                if tipo_consulta.startswith("insert"):
                    return cursor.lastrowid
                return cursor.rowcount
            except Exception as e:
                print("Error en MySQL:", e)
                return False
            finally:
                self.connection.close()

def conectar_mysql(nombre_bd):
    return MySQLConnection(nombre_bd)