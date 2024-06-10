# task_manager/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def task_list(request):
    """
    View to display a list of tasks.

    Redirects to the login page if the user is not authenticated.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Renders the task list template with the tasks.

    """
    if not request.user.is_authenticated:
        return redirect("login")
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
        "page_title": "List of tasks",
    }
    return render(request, "task_manager/task_list.html", context)


def task_detail(request, pk):
    """
    View to display details of a task.

    Args:
        request: HttpRequest object.
        pk: Primary key of the task to be displayed.

    Returns:
        HttpResponse: Renders the task detail template with the task.

    """
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_manager/task_detail.html", {"task": task})


def task_create(request):
    """
    View to create a new task.

    Redirects to the login page if the user is not authenticated.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Renders the task form template with the form.

    """
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "task_manager/task_form.html", {"form": form})


def task_update(request, pk):
    """
    View to update a task.

    Args:
        request: HttpRequest object.
        pk: Primary key of the task to be updated.

    Returns:
        HttpResponseRedirect: Redirects to the task list view.

    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task_manager/task_form.html", {"form": form})


def task_delete(request, pk):
    """
    View to delete a task.

    Args:
        request: HttpRequest object.
        pk: Primary key of the task to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the task list view.

    """
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task_list")


def register(request):
    """
    View to register a new user.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Renders the registration form.

    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "task_manager/register.html", {"form": form})


def login_view(request):
    """
    View to log in a user.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Renders the login form.

    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "task_manager/login.html", {"form": form})


def logout_view(request):
    """
    View to log out a user.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponseRedirect: Redirects to the index view.

    """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


def index(request):
    """
    View for the index page.

    Returns:
        HttpResponse: Renders the index page.

    """
    return render(request, "task_manager/index.html")
