# task_manager\forms.py
from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import (
    User,
)  # This is a default table for the database


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # The model for the app is the class Task.
        fields = [
            "title",
            "description",
            "deadline",
        ]  # Specifies the fields for the form.


class UserRegisterForm(
    UserCreationForm
):  # RegisterForm is inheriting from UserCreationForm
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
