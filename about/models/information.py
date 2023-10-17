from django.db import models
from django.core.exceptions import ValidationError


class Information(models.Model):
    data = models.TextField()

    class Meta:
        db_table = 'information'

    def __str__(self):
        return self.data
