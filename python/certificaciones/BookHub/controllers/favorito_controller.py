from flask import Blueprint, render_template, redirect, url_for, flash, session
from database import consultar_uno, consultar_todos, ejecutar
import pymysql


favorito_bp = Blueprint("favorito", __name__)


def usuario_logueado():
    return "usuario_id" in session


def mostrar_error_sesion():
    flash("Debes iniciar sesión para acceder a esta página.", "warning")
    return redirect(url_for("auth.index"))


@favorito_bp.route("/favoritos")
def mis_favoritos():
    if not usuario_logueado():
        return mostrar_error_sesion()

    libros = consultar_todos(
        """SELECT l.id, l.titulo, l.autor, l.genero, l.fecha_publicacion
           FROM favorito f
           JOIN libro l ON l.id = f.libro_id
           WHERE f.usuario_id = %s
           ORDER BY f.created_at DESC, f.id DESC""",
        (session["usuario_id"],),
    )

    return render_template("favoritos.html", libros=libros)


@favorito_bp.route("/favoritos/agregar/<int:libro_id>", methods=["POST"])
def agregar(libro_id):
    if not usuario_logueado():
        return mostrar_error_sesion()

    libro = consultar_uno("SELECT id FROM libro WHERE id = %s", (libro_id,))
    if not libro:
        flash("El libro no existe.", "danger")
        return redirect(url_for("libro.mis_libros"))

    try:
        ejecutar(
            "INSERT INTO favorito (usuario_id, libro_id) VALUES (%s, %s)",
            (session["usuario_id"], libro_id),
        )
        flash("Libro agregado a favoritos.", "success")
    except pymysql.err.IntegrityError:
        flash("Este libro ya está en tus favoritos.", "warning")

    return redirect(url_for("libro.detalle", libro_id=libro_id))


@favorito_bp.route("/favoritos/quitar/<int:libro_id>", methods=["POST"])
def quitar(libro_id):
    if not usuario_logueado():
        return mostrar_error_sesion()

    libro = consultar_uno("SELECT id FROM libro WHERE id = %s", (libro_id,))
    if not libro:
        flash("El libro no existe.", "danger")
        return redirect(url_for("libro.mis_libros"))

    filas, _ = ejecutar(
        "DELETE FROM favorito WHERE usuario_id = %s AND libro_id = %s",
        (session["usuario_id"], libro_id),
    )

    if filas > 0:
        flash("Libro eliminado de favoritos.", "success")
    else:
        flash("Este libro no estaba en tus favoritos.", "warning")

    return redirect(url_for("libro.detalle", libro_id=libro_id))
