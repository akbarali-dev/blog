from blog.models.base_model import BaseModel
from django.db import models


class Icon(BaseModel):
    name = models.CharField(max_length=100)
    code = models.TextField()

    class Meta:
        db_table = 'icon'
