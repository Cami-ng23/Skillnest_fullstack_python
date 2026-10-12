import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, consulta_sql, datos=None):
        with self.conexion.cursor_db() as cursor_db:
            try:
                cursor_db.execute(consulta_sql, datos)

                if consulta_sql.strip().lower().startswith("select"):
                    return cursor_db.fetchall()

                if consulta_sql.strip().lower().startswith("insert"):
                    return cursor_db.lastrowid

                return cursor_db.rowcount

            except Exception as e:
                print("Something went wrong:", e)
                return False

            finally:
                self.conexion.close()

def connectToMySQL(db):
    return MySQLConnection(db)