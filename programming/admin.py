from django.contrib import admin

from programming.models import Skills, Category, Portfolio

admin.site.register([Skills, Category, Portfolio])
