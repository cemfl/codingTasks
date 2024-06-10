from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Task
import datetime

class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(
            title = "Test Task",
            description = "This is a test task.",
            deadline = "2024-07-06",
            # created_at ="2024-06-07 12:04"
        )

    def test_task_has_title(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.title, "Test Task")

    def test_task_has_description(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.description, "This is a test task.")

    def test_task_has_deadline(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.deadline, datetime.date(2024, 7, 6))

class TaskViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            deadline="2024-07-06",
            # created_at="2024-06-07 12:04"
        )

    def test_task_list_view(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_detail_view(self):
        response = self.client.get(reverse("task_detail", args=[str(self.task.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertContains(response, "This is a test task.")

    def test_task_create_view(self):
        response = self.client.post(reverse("task_create"), {
            'title': "New Task",
            'description': "This is a new task.",
            'deadline': "2024-08-01"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("task_list"))
        self.assertTrue(Task.objects.filter(title="New Task").exists())

    def test_task_update_view(self):
        response = self.client.post(reverse("task_update", args=[str(self.task.id)]), {
            'title': "Updated Task",
            'description': "This task has been updated.",
            'deadline': "2024-09-01"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("task_list"))
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")

    def test_task_delete_view(self):
        response = self.client.post(reverse("task_delete", args=[str(self.task.id)]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("task_list"))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
