from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.materia import Materia
from flask_app.models.alumno import Alumno


@app.route("/alumnos/nuevo")
def nuevo_alumno():
    materias = Materia.listar()

    return render_template(
        "nuevo_alumno.html",
        materias=materias
    )


@app.route("/alumnos/crear", methods=["POST"])
def agregar_alumno():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    edad = request.form.get("edad", "").strip()
    materia_id = request.form.get("materia_id", "").strip()

    if not nombre or not apellido or not edad or not materia_id:
        return redirect(url_for("nuevo_alumno"))

    try:
        edad = int(edad)
        materia_id = int(materia_id)
    except ValueError:
        return redirect(url_for("nuevo_alumno"))

    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "materia_id": materia_id
    }

    Alumno.crear(datos)

    return redirect(url_for("materias"))
