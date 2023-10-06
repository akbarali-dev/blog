
from blog.models.base_model import BaseModel
from django.db import models


class Location(BaseModel):

    name = models.CharField(max_length=100)
    link = models.TextField()

    class Meta:
        db_table = 'location'
