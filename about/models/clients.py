from blog.models import User
from blog.models.base_model import BaseModel, PathAndRename
from django.db import models
from django.utils.html import mark_safe

path_and_rename = PathAndRename('about/clientsobj/image')


class Client(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=path_and_rename)
    description = models.TextField()

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "100"/>'.format(
            url=self.image.url
        ))

    img_preview.short_description = 'Image'

    class Meta:
        db_table = 'client'
