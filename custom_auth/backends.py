from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class JWTOrSessionAuthenticationBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = JWTAuthentication().authenticate(request)
        print(user)
        if user is not None:
            return user
        user = super().authenticate(request, username, password, **kwargs)
        return user
