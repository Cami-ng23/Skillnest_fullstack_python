from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "clave_secreta"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def guardar_datos():
    session["nombre"] = request.form["nombre"]
    session["edad"] = request.form["edad"]
    session["color"] = request.form["color"]
    session["animal"] = request.form["animal"]
    
    session["numero_suerte"] = random.randint(1, 99)
    
    frases = [
        "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
        "Una gran oportunidad laboral aparecerá pronto. Tu esfuerzo dará frutos.",
        "Un viaje inesperado te traerá grandes aprendizajes y momentos inolvidables.",
        "La fortuna estará de tu lado en los próximos días. Confía en tu intuición."
    ]
    session["prediccion"] = random.choice(frases)
    
    return redirect("/futuro")

@app.route("/futuro")
def mostrar_futuro():
    return render_template("futuro.html")

if __name__ == "__main__":
    app.run(debug=True)
