from flask import Flask

import Portfolio.main.models

from Portfolio.main.models import database, get_projects


def create_app():
    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = "Portfolio"

    init_database(app)

    from Portfolio.main.views import main
    app.register_blueprint(main, url_prefix="/")

    return app


def init_database(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
    database.init_app(app)

    with app.app_context():
        database.create_all()

        projects = get_projects()
        for project in projects:
            if not project.query.filter_by(name=project.name).first():
                database.session.add(project)

        database.session.commit()
