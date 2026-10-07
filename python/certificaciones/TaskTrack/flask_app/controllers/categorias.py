from flask import Blueprint, render_template, request, redirect, session, flash
from flask_app.models.categoria import Categoria

categorias_bp = Blueprint("categorias", __name__)

@categorias_bp.route("/categorias")
def listar():
    if "usuario_id" not in session:
        return redirect("/")

    categorias = Categoria.listar_usuario(session["usuario_id"])
    return render_template("categorias.html", categorias=categorias)

@categorias_bp.route("/categorias/crear", methods=["POST"])
def crear():
    if "usuario_id" not in session:
        return redirect("/")

    nombre = request.form["nombre"].strip()

    if len(nombre) < 2:
        flash("La categoría debe tener al menos 2 caracteres.", "error")
        return redirect("/categorias")

    Categoria.crear({
        "nombre": nombre,
        "usuario_id": session["usuario_id"]
    })

    flash("Categoría creada.", "success")
    return redirect("/categorias")

@categorias_bp.route("/categorias/editar/<int:id>", methods=["POST"])
def editar(id):
    if "usuario_id" not in session:
        return redirect("/")

    nombre = request.form["nombre"].strip()

    if len(nombre) < 2:
        flash("La categoría debe tener al menos 2 caracteres.", "error")
        return redirect("/categorias")

    Categoria.editar({
        "id": id,
        "nombre": nombre,
        "usuario_id": session["usuario_id"]
    })

    return redirect("/categorias")

@categorias_bp.route("/categorias/eliminar/<int:id>")
def eliminar(id):
    if "usuario_id" not in session:
        return redirect("/")

    Categoria.eliminar(id, session["usuario_id"])
    flash("Categoría eliminada.", "success")
    return redirect("/categorias")
