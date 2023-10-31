from blog.models import User
from blog.models.base_model import BaseModel
from django.db import models

# def send_bot_message(value)
class Contact(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    # print(
    #     "https://api.telegram.org/bot5489506404:AAGYYh1kOSFe-2dWhyemzbVlE6QH-eIveZY/sendMessage?chat_id=1474104201&text=saom")

    class Meta:
        db_table = 'contacts'
