from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave123"

@app.route("/")
def inicio():
    if "visitas" not in session:
        session["visitas"] = 0

    session["visitas"] += 1

    if "reinicios" not in session:
        session["reinicios"] = 0

    return render_template("index.html", visitas=session["visitas"], reinicios=session["reinicios"])

@app.route("/sumar_dos")
def sumar_dos():
    if "visitas" not in session:
        session["visitas"] = 0
    session["visitas"] += 2
    return redirect(url_for("inicio"))

@app.route("/reiniciar")
def reiniciar():
    session["visitas"] = 0
    session["reinicios"] = session.get("reinicios", 0) + 1
    return redirect(url_for("inicio"))

@app.route("/sumar", methods=["POST"])
def sumar():
    cantidad = int(request.form["cantidad"])
    session["visitas"] = session.get("visitas", 0) + cantidad
    return redirect(url_for("inicio"))

@app.route("/destruir_sesion")
def destruir():
    session.clear()
    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)
