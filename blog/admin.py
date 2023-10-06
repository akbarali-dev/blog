from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Blog, Goals, User

admin.site.register([Goals, User])


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("user", 'title', 'description', 'img_preview')
    readonly_fields = ['img_preview']
