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
            f"Name project '{context['project_name']}' include README and .gitignore for python",
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


class PipInstallRequirements(object):
    def run(self, context):
        steps = [
            "Press cmd+shift+P",
            "Select 'Python: Create Terminal'",
            "Double check for (.venv)",
            "Run 'pip install -r requirements.txt",
            "Requirements should include....",
            "Django, black, python-dotenv",
            "Run 'pip freeze requirements.txt'",
        ]
        print_steps(steps=steps)


class GenerateDjangoProject(object):
    def run(self, context):
        steps = [
            f"Run 'django-admin startproject {context['project_name']} .'",
            "the '.' is crucial to telling the script to install in the current directory",
        ]
        print_steps(steps=steps)


class DotEnv(object):
    def run(self, context):
        steps = [
            ".env Updates:",
            "Open settings.py",
            "Add 'from dotenv import load_dotenv'",
            "Add 'load_dotenv()",
            "Move the SECRET_KEY to a .env file in root",
            "Update settings.py SECRET_KEY=os.getenv('SECRET_KEY')",
        ]
        print_steps(steps=steps)


class SettingsConfig(object):
    def run(self, context):
        steps = [
            "Change settings.py",
            "Add 'import os'",
            "TIME_ZONE = 'America/Los_Angeles",
            "LANGUAGE_CODE = 'en-us",
            "STATIC_URL = '/static/",
            "STATIC_ROOT = BASE_DIR / 'static'",
            "ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']",
        ]
        print_steps(steps=steps)


class RunMigrations(object):
    def run(self, context):
        steps = [
            "Create the database, 'python manage.py migrate'",
        ]
        print_steps(steps=steps)


class VSCodeDebugLaunchFile(object):
    def run(self, context):
        steps = [
            "Navigate to debug window and select 'create a launch.json file",
            "Option: Django",
            "Try Running the debug and visiting 127.0.0.1:8000",
        ]
        print_steps(steps=steps)


class RunWebServer(object):
    def run(self, context):
        steps = [
            "Start the web server",
            "Run 'python manage.py runserver'",
        ]
        print_steps(steps=steps)


if __name__ == "__main__":
    context = {
        "project_name": input("Enter a project name: ") or "<project_name>",
    }
    procedure = [
        CreateGitHubRepository(),
        CloneRepository(),
        CreateVenv(),
        PipInstallRequirements(),
        GenerateDjangoProject(),
        DotEnv(),
        SettingsConfig(),
        RunMigrations(),
        VSCodeDebugLaunchFile(),
        RunWebServer(),
    ]
    for step in procedure:
        step.run(context)
    print("Done.")
