from blog.models.base_model import BaseModel
from django.db import models
from django.core.exceptions import ValidationError


def icon_name_case_check(value):
    if Icon.objects.filter(name__icontains=value.lower()):
        raise ValidationError("This name all ready exist")
    else:
        return value


class Icon(BaseModel):
    name = models.CharField(max_length=100, unique=True, validators=[icon_name_case_check])
    code = models.TextField()

    class Meta:
        db_table = 'icon'

    def __str__(self):
        return self.name
