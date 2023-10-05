from django.contrib.auth import get_user_model
from .base_model import BaseModel
from django.db import models

DjangoUser = get_user_model()


class User(BaseModel, models.Model):
    auth_user = models.ForeignKey(DjangoUser, models.CASCADE, )
    email = models.CharField(max_length=320)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(blank=False, null=False)
    job_name = models.CharField(max_length=155)

    class Meta:
        db_table = 'user'
