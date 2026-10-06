from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from models.usuario import Usuario
from database import consultar_uno, ejecutar


auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()


@auth_bp.route("/", methods=["GET"])
def index():
    if "usuario_id" in session:
        return redirect(url_for("libro.mis_libros"))
    return render_template("login.html", datos={})


@auth_bp.route("/registro", methods=["POST"])
def registro():
    datos, errores, password = Usuario.validar_registro(request.form)

    if not errores:
        usuario = consultar_uno("SELECT id FROM usuario WHERE email = %s", (datos["email"],))
        if usuario:
            errores.append("El correo ya está registrado.")

    if errores:
        for error in errores:
            flash(error, "danger")
        return render_template("login.html", datos=datos), 400

    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    ejecutar(
        "INSERT INTO usuario (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)",
        (datos["nombre"], datos["apellido"], datos["email"], password_hash),
    )

    flash("Cuenta creada correctamente. Ya puedes iniciar sesión.", "success")
    return redirect(url_for("auth.index"))


@auth_bp.route("/login", methods=["POST"])
def login():
    email, password, errores = Usuario.validar_login(request.form)

    if errores:
        for error in errores:
            flash(error, "danger")
        return render_template("login.html", datos={"login_email": email}), 400

    usuario = consultar_uno("SELECT * FROM usuario WHERE email = %s", (email,))

    if not usuario or not bcrypt.check_password_hash(usuario["password"], password):
        flash("El correo o contraseña son incorrectos.", "danger")
        return render_template("login.html", datos={"login_email": email}), 401

    session.clear()
    session["usuario_id"] = usuario["id"]
    session["usuario_nombre"] = usuario["nombre"]

    flash("Inicio de sesión exitoso.", "success")
    return redirect(url_for("libro.mis_libros"))


@auth_bp.route("/logout")
def logout():
    if "usuario_id" not in session:
        return redirect(url_for("auth.index"))

    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("auth.index"))
