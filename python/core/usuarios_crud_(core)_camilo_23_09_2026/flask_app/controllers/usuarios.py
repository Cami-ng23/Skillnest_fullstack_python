from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.usuario import Usuario


@app.route("/usuarios")
def index():
    usuarios = Usuario.get_all()
    return render_template("index.html", usuarios=usuarios)


@app.route("/usuarios/nuevo")
def nuevo():
    return render_template("nuevo.html")


@app.route("/usuarios/crear", methods=["POST"])
def crear():
    datos = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(datos)
    return redirect("/usuarios")


@app.route("/usuarios/<int:id>")
def detalle(id):
    datos = {"id": id}
    usuario = Usuario.get_by_id(datos)
    return render_template("detalle.html", usuario=usuario)


@app.route("/usuarios/editar/<int:id>")
def editar(id):
    datos = {"id": id}
    usuario = Usuario.get_by_id(datos)
    return render_template("editar.html", usuario=usuario)


@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar(id):
    datos = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.update(datos)
    return redirect("/usuarios")


@app.route("/usuarios/borrar/<int:id>")
def borrar(id):
    datos = {"id": id}
    Usuario.delete(datos)
    return redirect("/usuarios")
