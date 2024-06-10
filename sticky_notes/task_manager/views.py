# taskmanager/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout



# CRUD operations:
def task_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # Displays a list of all posts
    tasks = Task.objects.all()
    # A contect dictionary used to transfer data to the template.
    context = {
        "tasks": tasks,
        "page_title": "List of tasks",
    }
    return render(
        request, "task_manager/task_list.html", context
    )  # Shows the task list template with the tasks.


# Displays details of a task.
def task_detail(request, pk):
    task = get_object_or_404(
        Task, pk=pk
    )  # Retrieves the Task object by primary key or returns a 404 error.
    return render(
        request, "task_manager/task_detail.html", {"task": task}
    )  # Shows the task detail template with the tasks.


# View to create a new task.
def task_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = TaskForm(request.POST)  # Creates a form with submitted data.
        if form.is_valid():
            task = form.save(commit=False)  # Saves the form data to Task.
            task.save()  # Saves the task form to the database.
            return redirect("task_list")  # Returns to task list view.
    else:
        form = TaskForm()
    if not request.user.is_authenticated:
        return redirect('login')
    return render(
        request, "task_manager/task_form.html", {"form": form}
    )  # Shows the task form template with the tasks.


# View to update a task
def task_update(request, pk):
    task = get_object_or_404(
        Task, pk=pk
    )  # Retrieves the Task object by primary key or returns a 404 error.
    if request.method == "POST":
        form = TaskForm(
            request.POST, instance=task
        )  # Shows the task form with existing data.
        if form.is_valid():
            task = form.save(commit=False)  # Saves the form data to the task.
            task.save()  # Saves the task form to the database.
            return redirect("task_list")  # Returns to task list view.
    else:
        # Creates a TaskForm instance and returns the task form.
        form = TaskForm(instance=task)
    return render(
        request, "task_manager/task_form.html", {"form": form}
    )  # Shows the task form template with the tasks.

# View to delete a task.
def task_delete(request, pk):
    task = get_object_or_404(
        Task, pk=pk
    )  # Retrieves the Task object by primary key or returns a 404 error.
    task.delete()  # Deletes the task.
    return redirect("task_list")  # Returns to the task list view.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'task_manager/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('index')  # Go to Home page after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'task_manager/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('index')

def index(request): # For each page that DOES NOT need authentication
    return render(request, 'task_manager/index.html')
