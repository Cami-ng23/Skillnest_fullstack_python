from flask import Blueprint, render_template, request, redirect, session, flash
from flask_app.models.tarea import Tarea
from flask_app.models.categoria import Categoria
from datetime import date

tareas_bp = Blueprint("tareas", __name__)

def usuario_logueado():
    return "usuario_id" in session

def validar_tarea(form):
    titulo = form["titulo"].strip()
    descripcion = form["descripcion"].strip()
    fecha = form["fecha_limite"]
    categoria = form["categoria_id"]
    prioridad = form["prioridad"]

    if len(titulo) < 3:
        return "El título debe tener al menos 3 caracteres."

    if not categoria:
        return "Debes seleccionar una categoría."

    if not prioridad:
        return "Debes seleccionar una prioridad."

    if not fecha:
        return "Debes seleccionar una fecha."

    try:
        fecha_obj = date.fromisoformat(fecha)
        if fecha_obj < date.today():
            return "La fecha límite no puede ser pasada."
    except ValueError:
        return "La fecha no es válida."

    if len(descripcion) < 10:
        return "La descripción debe tener al menos 10 caracteres."

    return None

@tareas_bp.route("/dashboard")
def dashboard():
    if not usuario_logueado():
        return redirect("/")

    usuario_id = session["usuario_id"]
    estado = request.args.get("estado", "")
    buscar = request.args.get("buscar", "")

    tareas = Tarea.listar_usuario(usuario_id, estado, buscar)
    categorias = Categoria.listar_usuario(usuario_id)
    resumen = Tarea.contar_estados(usuario_id)

    cantidades = {"Pendiente": 0, "En progreso": 0, "Completada": 0}
    for item in resumen:
        cantidades[item["estado"]] = item["cantidad"]

    return render_template(
        "dashboard.html",
        tareas=tareas,
        categorias=categorias,
        cantidades=cantidades,
        estado=estado,
        buscar=buscar
    )

@tareas_bp.route("/tareas/nueva")
def nueva():
    if not usuario_logueado():
        return redirect("/")

    categorias = Categoria.listar_usuario(session["usuario_id"])
    return render_template("tarea_nueva.html", categorias=categorias)

@tareas_bp.route("/tareas/crear", methods=["POST"])
def crear():
    if not usuario_logueado():
        return redirect("/")

    error = validar_tarea(request.form)
    if error:
        flash(error, "error")
        return redirect("/tareas/nueva")

    Tarea.crear({
        "titulo": request.form["titulo"].strip(),
        "prioridad": request.form["prioridad"],
        "fecha_limite": request.form["fecha_limite"],
        "descripcion": request.form["descripcion"].strip(),
        "usuario_id": session["usuario_id"],
        "categoria_id": request.form["categoria_id"]
    })

    flash("Tarea creada correctamente.", "success")
    return redirect("/dashboard")

@tareas_bp.route("/tareas/<int:id>")
def detalle(id):
    if not usuario_logueado():
        return redirect("/")

    tarea = Tarea.buscar(id, session["usuario_id"])

    if not tarea:
        flash("No tienes permiso para ver esta tarea.", "error")
        return redirect("/dashboard")

    comentarios = Tarea.comentarios(id)
    return render_template("tarea_detalle.html", tarea=tarea, comentarios=comentarios)

@tareas_bp.route("/tareas/editar/<int:id>")
def editar_form(id):
    if not usuario_logueado():
        return redirect("/")

    tarea = Tarea.buscar(id, session["usuario_id"])

    if not tarea:
        flash("No tienes permiso para editar esta tarea.", "error")
        return redirect("/dashboard")

    categorias = Categoria.listar_usuario(session["usuario_id"])
    return render_template("tarea_editar.html", tarea=tarea, categorias=categorias)

@tareas_bp.route("/tareas/editar/<int:id>", methods=["POST"])
def editar(id):
    if not usuario_logueado():
        return redirect("/")

    tarea = Tarea.buscar(id, session["usuario_id"])
    if not tarea:
        flash("No tienes permiso para editar esta tarea.", "error")
        return redirect("/dashboard")

    error = validar_tarea(request.form)
    if error:
        flash(error, "error")
        return redirect(f"/tareas/editar/{id}")

    Tarea.editar({
        "id": id,
        "usuario_id": session["usuario_id"],
        "titulo": request.form["titulo"].strip(),
        "categoria_id": request.form["categoria_id"],
        "prioridad": request.form["prioridad"],
        "fecha_limite": request.form["fecha_limite"],
        "descripcion": request.form["descripcion"].strip(),
        "estado": request.form["estado"]
    })

    flash("Tarea actualizada.", "success")
    return redirect("/dashboard")

@tareas_bp.route("/tareas/eliminar/<int:id>")
def eliminar(id):
    if not usuario_logueado():
        return redirect("/")

    Tarea.eliminar(id, session["usuario_id"])
    flash("Tarea eliminada.", "success")
    return redirect("/dashboard")

@tareas_bp.route("/tareas/completar/<int:id>")
def completar(id):
    if not usuario_logueado():
        return redirect("/")

    Tarea.completar(id, session["usuario_id"])
    flash("Tarea marcada como completada.", "success")
    return redirect("/dashboard")

@tareas_bp.route("/tareas/<int:id>/comentario", methods=["POST"])
def comentario(id):
    if not usuario_logueado():
        return redirect("/")

    tarea = Tarea.buscar(id, session["usuario_id"])
    if not tarea:
        flash("No tienes permiso para comentar esta tarea.", "error")
        return redirect("/dashboard")

    comentario = request.form["comentario"].strip()

    if len(comentario) < 1:
        flash("El comentario no puede estar vacío.", "error")
        return redirect(f"/tareas/{id}")

    Tarea.agregar_comentario({
        "comentario": comentario,
        "usuario_id": session["usuario_id"],
        "tarea_id": id
    })

    return redirect(f"/tareas/{id}")
