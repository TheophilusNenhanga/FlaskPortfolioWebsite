from flask import Blueprint, render_template, send_file, abort

from Portfolio.main.models import Project

main = Blueprint("main", __name__)

strengths = ["Fast Learner", "Good Team Player", "Goal Oriented", "Self Motivated"]

programming_languages = [
    ["Python", 3],
    ["Java", 3],
    ["HTML+CSS", 2],
    ["JavaScript", 1]
]

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename: str):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route("/", methods=["GET", "POST"])
def home():
    project_db = Project.query.all()
    return render_template("home.html", projects=project_db, strengths=strengths, languages=programming_languages)


def create_project_route(project_name, motivation, about, skills, languages, template_name):
    @main.route(project_name, methods=["GET", "POST"], endpoint=f"{project_name}_endpoint")
    def project_function():
        return render_template(
            template_name,
            project_name=project_name,
            motivation=motivation,
            about=about,
            skills=skills,
            languages=languages
        )

    return project_function


@main.route("/download_resume", )
def download_resume():
    file_path = "static\\theophilus-nenhanga-resume.pdf"
    # if not allowed_file(file_path):
    # abort(403)
    return send_file(file_path, as_attachment=True)


# Create routes for individual projects
python_game_route = create_project_route(
    "Python Text Based Adventure Game",
    "This is the motivation\nThis is where I will write what motivated me to work on this project",
    "This is the about\nThis is where I will write what the project is about and a bit about how it works",
    "These are the skills that I showed in this project",
    ["Python"],
    "python_game.html"
)

java_game_route = create_project_route(
    "Java Text Based Adventure Game",
    "This is the motivation\nThis is where I will write what motivated me to work on this project",
    "This is the about\nThis is where I will write what the project is about and a bit about how it works",
    "These are the skills that I showed in this project",
    ["Java"],
    "java_game.html"
)

stats_route = create_project_route(
    "Statistics Visualization Website",
    "This is the motivation\nThis is where I will write what motivated me to work on this project",
    "This is the about\nThis is where I will write what the project is about and a bit about how it works",
    "These are the skills that I showed in this project",
    ["Python", "HTML", "CSS", "JavaScript"],
    "stats.html"
)

portfolio_route = create_project_route(
    "Portfolio Website",
    "This is the motivation\nThis is where I will write what motivated me to work on this project",
    "This is the about\nThis is where I will write what the project is about and a bit about how it works",
    "These are the skills that I showed in this project",
    ["Python", "HTML", "CSS", "JavaScript"],
    "portfolio.html"
)

# Register routes
main.add_url_rule("/projects/python-game", view_func=python_game_route, endpoint="python_game_endpoint")
main.add_url_rule("/projects/java-game", view_func=java_game_route, endpoint="java_game_endpoint")
main.add_url_rule("/projects/stats", view_func=stats_route, endpoint="stats_endpoint")
main.add_url_rule("/projects/portfolio", view_func=portfolio_route, endpoint="portfolio_endpoint")
