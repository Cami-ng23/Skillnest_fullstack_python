import os
import pymysql
from dotenv import load_dotenv
from flask import g

load_dotenv()


def get_connection():
    if "db" not in g:
        g.db = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "bookhub"),
            port=int(os.getenv("DB_PORT", "3306")),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )
    return g.db


def close_connection(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def consultar_uno(sql, parametros=()):
    with get_connection().cursor() as cursor:
        cursor.execute(sql, parametros)
        return cursor.fetchone()


def consultar_todos(sql, parametros=()):
    with get_connection().cursor() as cursor:
        cursor.execute(sql, parametros)
        return cursor.fetchall()


def ejecutar(sql, parametros=()):
    with get_connection().cursor() as cursor:
        cursor.execute(sql, parametros)
        return cursor.rowcount, cursor.lastrowid
