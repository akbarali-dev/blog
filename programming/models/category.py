from django.contrib.auth import get_user_model
from blog.models.base_model import BaseModel
from django.db import models

DjangoUser = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name
