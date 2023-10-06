from blog.models import User
from blog.models.base_model import BaseModel
from django.db import models


class Contact(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()

    class Meta:
        db_table = 'contact'
