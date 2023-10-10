from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as SuperUser
from .base_model import BaseModel, PathAndRename
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe

import re

DjangoUser = get_user_model()
path_and_rename = PathAndRename("blog/userobj/images/")


def check_phone(value):
    pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    if re.search(pattern, value):
        return value
    else:
        raise ValidationError(f'entered number {value} is in wrong format')


class User(BaseModel):
    auth_user = models.OneToOneField(DjangoUser, models.CASCADE, null=True, blank=True, related_name='user')
    user_name = models.CharField(unique=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=320)
    phone = models.CharField(max_length=15, validators=[check_phone])
    birth_date = models.DateField(blank=False, null=False)
    job_name = models.CharField(max_length=155)
    image = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    location = models.OneToOneField('about.Location', on_delete=models.CASCADE, unique=False, related_name='user')
    about = models.TextField()

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "100"/>'.format(
            url=self.image.url
        ))

    img_preview.short_description = 'Image'

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.full_name


def get_my_model_super_user():
    username = 'akbarali'
    if not SuperUser.objects.filter(username=username).exists():
        return None
    super_user = SuperUser.objects.get(username=username)
    if not super_user.user:
        return None
    return super_user.user
