import pymysql


class MySQLConnection:

    def __init__(self, base_datos):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database=base_datos,
            cursorclass=pymysql.cursors.DictCursor
        )

    def query_db(self, consulta, datos=None):
        cursor = self.connection.cursor()

        try:
            cursor.execute(consulta, datos)
            self.connection.commit()

            if consulta.strip().lower().startswith("select"):
                resultado = cursor.fetchall()
            else:
                resultado = cursor.lastrowid

            return resultado

        except Exception as error:
            print("Error:", error)
            return False

        finally:
            cursor.close()
            self.connection.close()
