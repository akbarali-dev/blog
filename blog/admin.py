from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register([Goals, CurrentProgress])


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("user", 'title', 'description', 'img_preview')
    readonly_fields = ['img_preview']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'phone', 'job_name', 'email')
