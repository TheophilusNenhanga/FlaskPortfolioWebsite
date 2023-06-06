from flask import Flask


def create_app():
    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = "Portfolio"

    from Portfolio.main.views import main
    app.register_blueprint(main, url_prefix="/")

    return app
