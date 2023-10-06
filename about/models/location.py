from blog.models import User
from blog.models.base_model import BaseModel
from django.db import models


class Location(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='location')
    name = models.CharField(max_length=100)
    link = models.TextField()

    class Meta:
        db_table = 'location'
