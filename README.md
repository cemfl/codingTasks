Welcome to the Task Manager App!

README Contents

1. Description
2. Installation
3. Credits

Description
- This is a simple task manager app created in a virtual Django environment.
It is an important part of my coding training as it is a culmination of everything I have learned
on my bootcamp and includes Python, HTML, CSS and javascript.

- Register an account to login and add tasks to your task list. Tasks can be created and including title,
description and deadline. A 'created at' note will be attached to each task.Tasks can be edited or deleted.

Installation - Ensure the latest version of Python is installed prior to this install
- Navigate to the folder your project will located in ('project_folder').
- Install Django using: pip install Django.
- Add the folder sticky_notes to this folder.
- Navigate to project_folder\sticky_notes\sticky_notes\settings.py
 - Add the app name 'task_manager' to the INSTALLED_APPS
- Navigate to project_folder\sticky_notes
- Run the initial database migrations to set up the database tables: python manage.py migrate
- Create a superuser to access the admin interface: python manage.py createsuperuser
- To view the app in the DJango development server: python manage.py runserver
- It will run on http://localhost:8000/
- To access the admin interface:http://localhost:8000/admin and login with the superuser credentials.

Credits
Created by Chris Fletcher (\cemfl) with the guidance of HyperionDev.
