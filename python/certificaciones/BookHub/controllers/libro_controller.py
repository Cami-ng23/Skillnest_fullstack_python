from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.libro import Libro
from database import consultar_uno, consultar_todos, ejecutar


libro_bp = Blueprint("libro", __name__)

BASE_LIBRO = """
    SELECT l.id, l.titulo, l.autor, l.genero, l.fecha_publicacion,
           l.descripcion, l.usuario_id,
           CONCAT(u.nombre, ' ', u.apellido) AS publicado_por,
           u.nombre AS publicador_nombre,
           (SELECT COUNT(*) FROM favorito f WHERE f.libro_id = l.id) AS total_favoritos
    FROM libro l
    JOIN usuario u ON u.id = l.usuario_id
"""


def usuario_logueado():
    return "usuario_id" in session


def mostrar_error_sesion():
    flash("Debes iniciar sesión para acceder a esta página.", "warning")
    return redirect(url_for("auth.index"))


@libro_bp.route("/libros")
def mis_libros():
    if not usuario_logueado():
        return mostrar_error_sesion()

    usuario_id = session["usuario_id"]

    mis_libros = consultar_todos(
        BASE_LIBRO + " WHERE l.usuario_id = %s ORDER BY l.created_at DESC, l.id DESC",
        (usuario_id,),
    )

    comunidad = consultar_todos(
        BASE_LIBRO + " WHERE l.usuario_id <> %s ORDER BY l.created_at DESC, l.id DESC",
        (usuario_id,),
    )

    return render_template("mis_libros.html", mis_libros=mis_libros, comunidad=comunidad)


@libro_bp.route("/explorar")
def explorar():
    if not usuario_logueado():
        return mostrar_error_sesion()

    comunidad = consultar_todos(
        BASE_LIBRO + " WHERE l.usuario_id <> %s ORDER BY l.created_at DESC, l.id DESC",
        (session["usuario_id"],),
    )

    return render_template("explorar.html", comunidad=comunidad)


@libro_bp.route("/libros/nuevo", methods=["GET", "POST"])
def nuevo():
    if not usuario_logueado():
        return mostrar_error_sesion()

    if request.method == "POST":
        datos, errores = Libro.validar(request.form)

        if errores:
            for error in errores:
                flash(error, "danger")
            return render_template("nuevo_libro.html", datos=datos, generos=Libro.GENEROS), 400

        ejecutar(
            """INSERT INTO libro
               (titulo, autor, genero, fecha_publicacion, descripcion, usuario_id)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (
                datos["titulo"], datos["autor"], datos["genero"],
                datos["fecha_publicacion"], datos["descripcion"],
                session["usuario_id"],
            ),
        )

        flash("Libro creado correctamente.", "success")
        return redirect(url_for("libro.mis_libros"))

    return render_template("nuevo_libro.html", datos={}, generos=Libro.GENEROS)


@libro_bp.route("/libros/<int:libro_id>")
def detalle(libro_id):
    if not usuario_logueado():
        return mostrar_error_sesion()

    libro = consultar_uno(BASE_LIBRO + " WHERE l.id = %s", (libro_id,))

    if not libro:
        flash("El libro no existe.", "danger")
        return redirect(url_for("libro.mis_libros"))

    usuarios_favoritos = consultar_todos(
        """SELECT u.id, u.nombre, u.apellido
           FROM favorito f
           JOIN usuario u ON u.id = f.usuario_id
           WHERE f.libro_id = %s
           ORDER BY f.created_at, f.id""",
        (libro_id,),
    )

    favorito = consultar_uno(
        "SELECT id FROM favorito WHERE usuario_id = %s AND libro_id = %s",
        (session["usuario_id"], libro_id),
    )

    return render_template(
        "detalle_libro.html",
        libro=libro,
        usuarios_favoritos=usuarios_favoritos,
        es_favorito=favorito is not None,
    )


@libro_bp.route("/libros/editar/<int:libro_id>", methods=["GET", "POST"])
def editar(libro_id):
    if not usuario_logueado():
        return mostrar_error_sesion()

    usuario_id = session["usuario_id"]

    libro = consultar_uno(
        "SELECT * FROM libro WHERE id = %s AND usuario_id = %s",
        (libro_id, usuario_id),
    )

    if not libro:
        existe = consultar_uno("SELECT id FROM libro WHERE id = %s", (libro_id,))
        if existe:
            flash("No tienes permisos para realizar esta acción.", "danger")
        else:
            flash("El libro no existe.", "danger")
        return redirect(url_for("libro.mis_libros"))

    if request.method == "POST":
        datos, errores = Libro.validar(request.form)

        if errores:
            for error in errores:
                flash(error, "danger")
            return render_template(
                "editar_libro.html",
                libro=libro,
                datos=datos,
                generos=Libro.GENEROS,
            ), 400

        ejecutar(
            """UPDATE libro
               SET titulo = %s, autor = %s, genero = %s,
                   fecha_publicacion = %s, descripcion = %s
               WHERE id = %s AND usuario_id = %s""",
            (
                datos["titulo"], datos["autor"], datos["genero"],
                datos["fecha_publicacion"], datos["descripcion"],
                libro_id, usuario_id,
            ),
        )

        flash("Libro actualizado correctamente.", "success")
        return redirect(url_for("libro.mis_libros"))

    datos = {
        "titulo": libro["titulo"],
        "autor": libro["autor"],
        "genero": libro["genero"],
        "fecha_publicacion": libro["fecha_publicacion"].isoformat(),
        "descripcion": libro["descripcion"],
    }

    return render_template(
        "editar_libro.html",
        libro=libro,
        datos=datos,
        generos=Libro.GENEROS,
    )


@libro_bp.route("/libros/eliminar/<int:libro_id>", methods=["POST"])
def eliminar(libro_id):
    if not usuario_logueado():
        return mostrar_error_sesion()

    usuario_id = session["usuario_id"]

    libro = consultar_uno(
        "SELECT id FROM libro WHERE id = %s AND usuario_id = %s",
        (libro_id, usuario_id),
    )

    if not libro:
        existe = consultar_uno("SELECT id FROM libro WHERE id = %s", (libro_id,))
        if existe:
            flash("No tienes permisos para realizar esta acción.", "danger")
        else:
            flash("El libro no existe.", "danger")
        return redirect(url_for("libro.mis_libros"))

    ejecutar("DELETE FROM libro WHERE id = %s AND usuario_id = %s", (libro_id, usuario_id))
    flash("Libro eliminado correctamente.", "success")
    return redirect(url_for("libro.mis_libros"))
