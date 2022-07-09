import sys


def print_steps(steps):
    for step in steps:
        print(f"- {step}")
    input("Press Enter to continue: \n")


class CreateGitHubRepository:
    def run(self, context):
        steps = [
            "Log into GitHub",
            "Create a new project",
            f"Name project '{context['project_name']}' include README and .gitignore for python",
        ]
        print_steps(steps=steps)


class CloneRepository:
    def run(self, context):
        steps = [
            "Open VSCode and press cmd+shift+P",
            "Search & select 'Git: Clone'",
            "Select option for GitHub",
            "Select project & a destination",
        ]
        print_steps(steps=steps)


class CreateVenv:
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


class PipInstallRequirements:
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


class GenerateDjangoProject:
    def run(self, context):
        steps = [
            f"Run 'django-admin startproject {context['project_name']}'",
        ]
        print_steps(steps=steps)


class DotEnv:
    def run(self, context):
        steps = [
            ".env Updates:",
            "Open settings.py",
            "Add 'import os'",
            "Add 'from dotenv import load_dotenv'",
            "Add 'load_dotenv()",
            "Move the SECRET_KEY to a .env file in root",
            "Update settings.py SECRET_KEY=os.getenv('SECRET_KEY')",
        ]
        print_steps(steps=steps)


class CreateNewApp:
    def run(self, context):
        steps = [
            "Change to the project directory",
            "Run 'python3 manage.py startapp <appname>'",
            "add to settings.py/INSTALLED_APPS '<appname>.apps.<App>Config'",
        ]
        print_steps(steps=steps)


class CreateTemplatesFolder:
    def run(self, context):
        steps = [
            "Create 'templates' folder at the same directory level as the app",
            "In settings.py, add to TEMPLATES: 'DIRS': [BASE_DIR / 'templates'],  # new",
        ]
        print_steps(steps=steps)


class SettingsConfig:
    def run(self, context):
        steps = [
            "Change settings.py",
            "TIME_ZONE = 'America/Los_Angeles",
            "LANGUAGE_CODE = 'en-us",
            # "STATIC_URL = 'static/",
            # "STATIC_ROOT = BASE_DIR / 'static'",
            # "ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']",
        ]
        print_steps(steps=steps)


class RunMigrations:
    def run(self, context):
        steps = [
            "Create the database, 'python manage.py migrate'",
        ]
        print_steps(steps=steps)


class VSCodeDebugLaunchFile:
    def run(self, context):
        steps = [
            "Navigate to debug window and select 'create a launch.json file",
            "Option: Django",
            "Try Running the debug and visiting 127.0.0.1:8000",
        ]
        print_steps(steps=steps)


class RunWebServer:
    def run(self, context):
        steps = [
            "Start the web server",
            "Run 'python manage.py runserver'",
        ]
        print_steps(steps=steps)


if __name__ == "__main__":
    context = {
        "project_name": "<project_name>",
        "app_name": "<app_name>",
    }
    procedure = [
        CreateGitHubRepository(),
        CloneRepository(),
        CreateVenv(),
        PipInstallRequirements(),
        GenerateDjangoProject(),
        DotEnv(),
        CreateNewApp(),
        CreateTemplatesFolder(),
        SettingsConfig(),
        RunMigrations(),
        VSCodeDebugLaunchFile(),
        RunWebServer(),
    ]
    for step in procedure:
        step.run(context)
    print("Done.")
