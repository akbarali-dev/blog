from django.contrib import admin

from programming.models import Skills, Category, Portfolio, Experience, Technology

admin.site.register([Skills, Category, Portfolio, Experience, Technology])
