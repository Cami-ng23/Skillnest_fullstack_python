from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "clave_secreta"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    session["nombre"] = request.form["nombre"]
    session["edad"] = request.form["edad"]
    session["color"] = request.form["color"]
    session["animal"] = request.form["animal"]

    return redirect("/futuro")


@app.route("/futuro")
def futuro():
    nombre = session.get("nombre")
    edad = session.get("edad")
    color = session.get("color")
    animal = session.get("animal")

    mensajes = [
        "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
        "Un nuevo desafío llegará a tu vida y te ayudará a descubrir algo importante sobre ti.",
        "Las estrellas anuncian una etapa de cambios positivos y nuevas oportunidades.",
        "Una sorpresa inesperada cambiará tu día y traerá mucha felicidad."
    ]

    prediccion = random.choice(mensajes)
    numero_suerte = random.randint(1, 99)

    return render_template(
        "futuro.html",
        nombre=nombre,
        edad=edad,
        color=color,
        animal=animal,
        prediccion=prediccion,
        numero_suerte=numero_suerte
    )


if __name__ == "__main__":
    app.run(debug=True)
