from .base_model import BaseModel, PathAndRename
from django.db import models
from django.utils.html import mark_safe

from . import User

path_and_rename = PathAndRename("blog/blogobj/images/")


class CurrentProgress(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_progress')
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.TextField()

    class Meta:
        db_table = 'current_progress'
