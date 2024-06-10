# task_manager/urls.py
from django.urls import path
from .views import (
    task_list,
    task_detail,
    task_create,
    task_update,
    task_delete,
    register,
    login_view,
    logout_view,
    index,
)


urlpatterns = [
    path("", index, name="index"),
    # URL pattern for displaying details of a specific task.
    path("task/<int:pk>/", task_detail, name="task_detail"),
    # URL pattern for creating a new task.
    path("task/new/", task_create, name="task_create"),
    # URL pattern for updating an existing task.
    path("task/<int:pk>/edit/", task_update, name="task_update"),
    # URL pattern for deleting an existing task.
    path("task/<int:pk>/delete/", task_delete, name="task_delete"),
    # # URL pattern for registering user.
    path("register/", register, name="register"),
    # URL pattern for login.
    path("login/", login_view, name="login"),
    # URL pattern for logout.
    path("logout/", logout_view, name="logout"),
    # URL pattern for index.
    path("index/", index, name="index"),
    # URL pattern for logout.
    path("task_list/", task_list, name="task_list"),
]
