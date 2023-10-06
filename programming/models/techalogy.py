from django.contrib.auth import get_user_model

from blog.models import User
from blog.models.base_model import BaseModel, IntegerRangeField
from django.db import models

DjangoUser = get_user_model()


class Technology(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    discount = IntegerRangeField(max_value=100, min_value=0)

    class Meta:
        db_table = 'technalogy'
