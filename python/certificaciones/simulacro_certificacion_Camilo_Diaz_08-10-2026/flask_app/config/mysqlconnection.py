import pymysql

def conectar():
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password=1234,
        database="donacion_peluches"
    )
    return conexion