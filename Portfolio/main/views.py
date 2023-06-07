from flask import Blueprint, render_template

main = Blueprint("main", __name__)

projects = {0: ["name", "date", "language(s)", "description", "link", "learn more link"],
            1: ["Python Text Based Adventure Game", "December 2020", "Python",
                "A text based adventure game made in Python", "https://github.com/TeeEnnEnn/Text-Based-Adventure-Game",
                "/projects/python-game"],
            2: ["Statistics Website Clone", "August 2023", "Python, HTML, CSS, JavaScript",
                "A website that handles small datasets", "https://github.com/TeeEnnEnn/StatisticsWebsiteClone",
                "/projects/stats"],
            3: ["Java text Based Adventure Game", "May 2023", "Java", "A text based adventure game made in Java",
                "https://github.com/TeeEnnEnn/Java-Text-Based-Game", "/projects/java-game"],
            4: ["Portfolio Website", "July 2023", "Python, HTML, CSS, Javascript",
                "A portfolio website showcasing some of the work i have done",
                "https://github.com/TeeEnnEnn/PortfolioWebsite", "/projects/portfolio"],
            5: ["More To Come", " ", "", " ", "https://github.com/TeeEnnEnn", "https://github.com/TeeEnnEnn"]}

strengths = ["Fast Learner", "Good Team Player", "Goal Oriented", "Self Motivated"]

weaknesses = ["Weak Design Skills"]

languages = [["Python", 3], ["Java", 3], ["HTML+CSS", 2], ["JavaScript", 1]]


@main.route("/", methods=["GET", "POST"])
def home():
    project_length = len(projects) - 1
    return render_template("home.html", project_variable=projects, strength_variable=strengths,
                           weakness_variable=weaknesses, project_length=project_length, languages=languages)


@main.route("/projects/python-game", methods=["GET", "POST"])
def python_game():
    return render_template("python_game.html")


@main.route("/projects/java-game", methods=["GET", "POST"])
def java_game():
    return render_template("java_game.html")


@main.route("/projects/stats", methods=["GET", "POST"])
def stats():
    return render_template("stats.html")


@main.route("/projects/portfolio", methods=["GET", "POST"])
def portfolio():
    return render_template("portfolio.html")
