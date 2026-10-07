from flask import Flask
from flask_bcrypt import Bcrypt
from flask import session
from flask_app.controllers.usuarios import usuarios_bp
from flask_app.controllers.tareas import tareas_bp
from flask_app.controllers.categorias import categorias_bp

app = Flask(__name__, template_folder="flask_app/templates", static_folder="flask_app/static")
app.secret_key = "tasktrack123"

bcrypt = Bcrypt(app)

app.register_blueprint(usuarios_bp)
app.register_blueprint(tareas_bp)
app.register_blueprint(categorias_bp)

if __name__ == "__main__":
    app.run(debug=True)