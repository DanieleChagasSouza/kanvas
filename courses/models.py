from django.db import models
from uuid import uuid4
from students_courses.models import StudentCourse


class Choices(models.TextChoices):
    DEFAULT = ("not started",)
    IN_PROGRESS = ("in progress",)
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11, choices=Choices.choices, default=Choices.DEFAULT
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.PROTECT,
        related_name="courses",
        null=True,
        blank=True,
    )
    students = models.ManyToManyField(
        "accounts.Account", through=StudentCourse, related_name="my_courses"
    )
