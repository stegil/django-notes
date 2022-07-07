import sys


def print_steps(steps):
    for step in steps:
        print(f"- {step}")
    input("Press Enter to continue: ")


class CreateGitHubRepository(object):
    def run(self, context):
        steps = [
            "Log into GitHub",
            "Create a new project",
            "Name project, include README and .gitignore for python",
        ]
        print_steps(steps=steps)


class CloneRepository(object):
    def run(self, context):
        steps = [
            "Open VSCode and press cmd+shift+P",
            "Search & select 'Git: Clone'",
            "Select option for GitHub",
            "Select project & a destination",
        ]
        print_steps(steps=steps)


class CreateVenv(object):
    def run(self, context):
        steps = [
            "Press cmd+shift+P",
            "Select a Python Interpreter",
            "Press cmd+shift+P",
            "Select 'Python: Create Terminal'",
            "Run 'python3 -m venv .venv",
            "Select the virtual environment for the Python interpreter",
            "Close python terminal(s)",
        ]
        print_steps(steps=steps)


class RunCookieCutter(object):
    def run(self, context):
        steps = [
            "Press cmd+shift+P",
            "Select 'Python: Create Terminal'",
            "Double check for (.venv)",
            "Run 'pip install cookiecutter",
            "Run 'cookiecutter https://github.com/feldroy/django-crash-starter.git'",
        ]
        print_steps(steps=steps)


class PipInstallRequirements(object):
    def run(self, context):
        steps = [
            "Press cmd+shift+P",
            "Select 'Python: Create Terminal'",
            "Double check for (.venv)",
            "Run 'pip install -r requirements.txt",
            "Requirements should include....",
            "Django, python-dotenv, black ",
            "If installed manually, run 'pip freeze requirements.txt'",
        ]
        print_steps(steps=steps)


class DotEnv(object):
    def run(self, context):
        steps = [
            "TODO: Set up .env for the SECRET_KEY and any other important env variables",
        ]
        print_steps(steps=steps)


if __name__ == "__main__":
    context = {}
    procedure = [
        CreateGitHubRepository(),
        CloneRepository(),
        CreateVenv(),
        PipInstallRequirements(),
        DotEnv(),  # TODO
    ]
    for step in procedure:
        step.run(context)
    print("Done.")
