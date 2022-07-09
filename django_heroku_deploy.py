import sys


def print_steps(steps):
    for step in steps:
        print(f"{step}")
    input("Press Enter to continue: \n")


class InstallHomebrew:
    def run(self, context):
        steps = [
            "Install Homebrew - https://brew.sh",
        ]
        print_steps(steps=steps)


class InstallHeroku:
    def run(self, context):
        steps = [
            "In Terminal, enter: ",
            "   brew tap heroku/brew && brew install heroku",
            "from: https://devcenter.heroku.com/articles/heroku-cli",
        ]
        print_steps(steps=steps)


class InstallGunicorn:
    def run(self, context):
        steps = [
            "In a Python terminal...",
            "   'python -m pip install gunicorn'",
            "   'python -m pip freeze > requirements.txt'",
        ]
        print_steps(steps=steps)


class ChangeAllowedHosts:
    def run(self, context):
        steps = [
            "Open django_project/settings.py",
            "   ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']",
        ]
        print_steps(steps=steps)


class CreateProcfile:
    def run(self, context):
        steps = [
            "Create Procfile.txt in the base directory, next to manage.py with the content:",
            "web: gunicorn django_project.wsgi --log-file -",
        ]
        print_steps(steps=steps)


class CreateRuntimeFile:
    def run(self, context):
        steps = [
            "Create runtime.txt file in the base directory, next to manage.py with the python version:",
            "python-3.10.2",
        ]
        print_steps(steps=steps)


class HerokuLogin:
    def run(self, context):
        steps = [
            "In a (.venv) Shell terminal window, type 'heroku login'",
        ]
        print_steps(steps=steps)


class HerokuDeploy:
    def run(self, context):
        steps = [
            "In a (.venv) Shell terminal window...",
            "   'heroku create'",
            "   Verfiy with 'git remote -v'",
            "To ignore static files...",
            "   'heroku config:set DISABLE_COLLECTSTATIC=1'",
            "Push code up to Heroku (2 options):",
            "   'git push heroku main' to push everything up",
            "   'git subtree push --prefix path/to/directory heroku main'",
        ]
        print_steps(steps=steps)


if __name__ == "__main__":
    context = {}
    procedure = [
        InstallHomebrew(),
        InstallGunicorn(),
        ChangeAllowedHosts(),
        CreateProcfile(),
        CreateRuntimeFile(),
        HerokuLogin(),
    ]
    for step in procedure:
        step.run(context)
    print("Done.")
