from flask_app import app

from flask_app.controllers import materias
from flask_app.controllers import alumnos


if __name__ == "__main__":
    app.run(debug=True)
