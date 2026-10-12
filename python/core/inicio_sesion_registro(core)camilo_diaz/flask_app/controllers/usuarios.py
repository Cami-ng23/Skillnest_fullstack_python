from flask import render_template, redirect, request, url_for, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Ruta raiz
@app.route("/")
def index():
    if 'usuario_id' in session:
        return redirect(url_for('inicio'))
    return redirect(url_for('mostrar_login'))

# Ruta mostrar registro
@app.route("/registrarse")
def mostrar_registro():
    if 'usuario_id' in session:
        return redirect(url_for('inicio'))
    return render_template("registrarse.html")

# Ruta mostrar login
@app.route("/iniciar_sesion")
def mostrar_login():
    if 'usuario_id' in session:
        return redirect(url_for('inicio'))
    return render_template("iniciar_sesion.html")

# Ruta procesar registro
@app.route("/registrar", methods=["POST"])
def registrar():
    if not Usuario.validar_registro(request.form):
        return redirect(url_for('mostrar_registro'))
    
    clave_encriptada = bcrypt.generate_password_hash(request.form['password'])
    
    datos = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip(),
        "password": clave_encriptada
    }
    
    usuario_id = Usuario.save(datos)
    session['usuario_id'] = usuario_id  
    return redirect(url_for('inicio'))

# Ruta procesar login
@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.get_by_email(request.form['email'])
    
    if not usuario or not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Credenciales inválidas.", "login")
        return redirect(url_for('mostrar_login'))
        
    session['usuario_id'] = usuario.id  
    return redirect(url_for('inicio'))

# Ruta inicio exito
@app.route("/inicio")
def inicio():
    if 'usuario_id' not in session:
        return redirect(url_for('mostrar_login'))
        
    usuario_actual = Usuario.get_by_id(session['usuario_id'])
    return render_template("inicio.html", usuario=usuario_actual)

# Ruta logout
@app.route("/logout")
def logout():
    session.clear()  
    return redirect(url_for('mostrar_login'))