from django.contrib.auth import get_user_model

from blog.models import User
from blog.models.base_model import BaseModel
from django.db import models

from programming.models import Category

DjangoUser = get_user_model()


class Portfolio(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category)

    class Meta:
        db_table = 'portfolio'

    def __str__(self):
        return self.name
