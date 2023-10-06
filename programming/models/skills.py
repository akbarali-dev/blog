from django.contrib.auth import get_user_model

from blog.models import User
from blog.models.base_model import BaseModel, IntegerRangeField
from django.db import models

from programming.models.techalogy import Technology

DjangoUser = get_user_model()


class Skills(BaseModel):
    name = models.CharField(max_length=100)
    discount = IntegerRangeField(max_value=100, min_value=0)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='skills')

    class Meta:
        db_table = 'skills'
