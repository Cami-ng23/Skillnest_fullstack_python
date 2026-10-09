from flask import Flask, flash, redirect, session, url_for
from database import close_connection
from controllers.auth_controller import auth_bp
from controllers.libro_controller import libro_bp
from controllers.favorito_controller import favorito_bp
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "clave-bookhub-cambiar-en-env")
    app.teardown_appcontext(close_connection)

    app.register_blueprint(auth_bp)
    app.register_blueprint(libro_bp)
    app.register_blueprint(favorito_bp)

    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        flash("La página que buscas no existe.", "danger")
        if "usuario_id" in session:
            return redirect(url_for("libro.mis_libros"))
        return redirect(url_for("auth.index"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
