from django.contrib.auth import get_user_model

from blog.models import User
from blog.models.base_model import BaseModel, PathAndRename
from django.db import models
from django.utils.html import mark_safe

from programming.models import Category

path_and_rename = PathAndRename("blog/blogobj/images/")

DjangoUser = get_user_model()


class Portfolio(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to=path_and_rename)

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "100"/>'.format(
            url=self.image.url
        ))

    img_preview.short_description = 'Image'

    class Meta:
        db_table = 'portfolio'

    def __str__(self):
        return self.name
