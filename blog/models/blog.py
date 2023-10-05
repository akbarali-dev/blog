from .base_model import BaseModel
from django.db import models

from . import User


class Blog(BaseModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'blog'
