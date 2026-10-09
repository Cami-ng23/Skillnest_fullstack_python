import pymysql
import pymysql.cursors


class MySQLConnection:
    def __init__(self, base):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database=base,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, consulta, datos=None):
        with self.connection.cursor() as db_cursor:
            try:
                db_cursor.execute(consulta, datos or {})
                tipo = consulta.strip().lower()

                if tipo.startswith("select"):
                    return db_cursor.fetchall()

                if tipo.startswith("insert"):
                    return db_cursor.lastrowid

                return db_cursor.rowcount

            except Exception as error:
                print("Error en MySQL:", error)
                return False

            finally:
                self.connection.close()


def connectToMySQL(base):
    return MySQLConnection(base)
