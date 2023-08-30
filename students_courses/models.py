from django.db import models
from uuid import uuid4


class Choices(models.TextChoices):
    DEFAULT = ("pending",)
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    status = models.CharField(choices=Choices.choices, default=Choices.DEFAULT)
    student = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="students_courses"
    )
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="students_courses"
    )
