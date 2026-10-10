from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/estudiantes/nuevo")
def nuevo_estudiante():
    lista_cursos = Curso.get_all()
    return render_template("nuevo_estudiante.html", cursos=lista_cursos)

@app.route("/estudiantes/crear", methods=["POST"])
def crear_estudiante():
    nombre_estudiante = request.form.get("nombre", "").strip()
    apellido_estudiante = request.form.get("apellido", "").strip()
    edad_texto = request.form.get("edad", "").strip()
    id_curso_texto = request.form.get("curso_id", "").strip()

    if not nombre_estudiante or not apellido_estudiante or not edad_texto or not id_curso_texto:
        return redirect(url_for("nuevo_estudiante"))

    try:
        edad_numero = int(edad_texto)
        id_curso = int(id_curso_texto)
    except ValueError:
        return redirect(url_for("nuevo_estudiante"))

    datos_estudiante = {
        "nombre": nombre_estudiante,
        "apellido": apellido_estudiante,
        "edad": edad_numero,
        "curso_id": id_curso
    }
    Estudiante.save(datos_estudiante)
    return redirect(url_for("cursos"))