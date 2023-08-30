from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class Account(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
