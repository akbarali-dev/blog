from django.contrib.auth import get_user_model


from .base_model import BaseModel, PathAndRename
from django.db import models

DjangoUser = get_user_model()
path_and_rename = PathAndRename("blog/userobj/images/")


class User(BaseModel):
    auth_user = models.ForeignKey(DjangoUser, models.CASCADE, )
    email = models.CharField(max_length=320)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(blank=False, null=False)
    job_name = models.CharField(max_length=155)
    image = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    location = models.OneToOneField('about.Location', on_delete=models.CASCADE)

    about = models.TextField()

    class Meta:
        db_table = 'user'
