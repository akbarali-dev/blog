from about.models import Icon
from blog.models import User
from blog.models.base_model import BaseModel
from django.db import models


class SocialNetwork(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_network')
    name = models.CharField(max_length=100)
    link = models.TextField()
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'social_network'
