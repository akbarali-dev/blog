from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser for the Django application.'

    def handle(self, *args, **options):
        username = 'akbarali'
        email = 'admin@example.com'
        password = 'adminpassword'
        print("HELLO                              HELLO")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
