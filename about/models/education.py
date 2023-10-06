from blog.models import User
from blog.models.base_model import BaseModel
from django.db import models


class Education(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    graduation_year = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'education'

    def __str__(self):
        return self.name
