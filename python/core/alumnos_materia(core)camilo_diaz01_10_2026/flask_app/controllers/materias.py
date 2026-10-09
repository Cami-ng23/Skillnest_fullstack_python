from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.materia import Materia


@app.route("/")
def inicio():
    return redirect(url_for("materias"))


@app.route("/materias")
def materias():
    lista_materias = Materia.listar()

    return render_template(
        "materias.html",
        materias=lista_materias
    )


@app.route("/materias/crear", methods=["POST"])
def agregar_materia():
    nombre = request.form.get("nombre", "").strip()

    if not nombre:
        return redirect(url_for("materias"))

    datos = {
        "nombre": nombre
    }

    Materia.crear(datos)

    return redirect(url_for("materias"))


@app.route("/materias/<int:id>")
def ver_materia(id):
    materia = Materia.obtener_materia_con_alumnos(id)

    if materia is None:
        return redirect(url_for("materias"))

    return render_template(
        "ver_materia.html",
        materia=materia
    )
