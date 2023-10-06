from blog.models import User
from blog.models.base_model import BaseModel
from django.db import models


class About(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='about')
    description = models.TextField()

    class Meta:
        db_table = 'about'
