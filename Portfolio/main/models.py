from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


class Project(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), unique=True)
    date = database.Column(database.String(50))
    languages = database.Column(database.String(200))
    description = database.Column(database.String(200))
    link = database.Column(database.String(200))
    learn_more_link = database.Column(database.String(200))

    def __init__(self, name, date, languages, description, link, learn_more_link):
        self.name = name
        self.date = date
        self.languages = languages
        self.description = description
        self.link = link
        self.learn_more_link = learn_more_link


def get_projects():
    projects = [
        Project("Python Text Based Adventure Game",
                "December 2020",
                "Python",
                "A text based adventure game made in Python",
                "https://github.com/TeeEnnEnn/Text-Based-Adventure-Game",
                "/projects/python-game"),

        Project("Statistics Website Clone",
                "August 2023",
                "Python, HTML, CSS, JavaScript",
                "A website that handles small datasets", "https://github.com/TeeEnnEnn/StatisticsWebsiteClone",
                "/projects/stats"),

        Project("Java text Based Adventure Game",
                "May 2023",
                "Java",
                "A text based adventure game made in Java",
                "https://github.com/TeeEnnEnn/Java-Text-Based-Game",
                "/projects/java-game"),

        Project("Portfolio Website",
                "July 2023",
                "Python, HTML, CSS, Javascript",
                "A portfolio website showcasing some of the work I have done",
                "https://github.com/TeeEnnEnn/PortfolioWebsite", "/projects/portfolio"),

        Project("More To Come", "", "", "", "https://github.com/TeeEnnEnn", "https://github.com/TeeEnnEnn")
    ]
    return projects
