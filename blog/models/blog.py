from .base_model import BaseModel, PathAndRename
from django.db import models
from django.utils.html import mark_safe

from . import User

path_and_rename = PathAndRename("blog/blogobj/images/")


class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=path_and_rename, null=True, blank=True)

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "100"/>'.format(
            url=self.image.url
        ))

    img_preview.short_description = 'Image'

    class Meta:
        db_table = 'blog'
