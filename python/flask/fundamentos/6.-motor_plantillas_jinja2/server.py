from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template(
        "index.html",

        nombre="Daniel",

        curso="Desarrollo Web con Flask",

        ciudad= "Santiago",

        anio= 2026,

        profesor = false,
        
        tecnologias=[
        "Python",
        "Flask",
        "HTML",
        "CSS"
    ]
    )
    
@app.route("/jugador")
def jugador():
    return render_template(

    "index.html",

    jugador="Camilo",

    puntaje=9200,

    lider=True

)

if __name__ == "__main__":

    app.run(debug=True)
    