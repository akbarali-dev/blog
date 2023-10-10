from django.contrib.auth import get_user_model
from .base_model import BaseModel
from django.db import models

from . import User

DjangoUser = get_user_model()


class Goal(BaseModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=125)
    description = models.TextField()
    icon = models.TextField()

    class Meta:
        db_table = 'goal'
