from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.curso import Curso

@app.route("/")
def inicio():
    return redirect(url_for("cursos"))

@app.route("/cursos")
def cursos():
    lista_cursos = Curso.get_all()
    return render_template("cursos.html", cursos=lista_cursos)

@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    nombre_curso = request.form.get("nombre", "").strip()
    if not nombre_curso:
        return redirect(url_for("cursos"))
    
    datos_curso = {"nombre": nombre_curso}
    Curso.save(datos_curso)
    return redirect(url_for("cursos"))

@app.route("/cursos/<int:id>")
def mostrar_curso(id):
    detalle_curso = Curso.get_curso_con_estudiantes(id)
    if detalle_curso is None:
        return redirect(url_for("cursos"))
    return render_template("mostrar_curso.html", curso=detalle_curso)