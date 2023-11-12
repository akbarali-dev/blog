from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("user", 'title', 'description', 'img_preview')
    search_fields = ('user', 'title')
    autocomplete_fields = ('user',)
    readonly_fields = ['img_preview']
    list_per_page = 15


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user_name', 'phone', 'job_name', 'email', 'img_preview',)
    search_fields = ('full_name', 'phone', 'job_name', 'email', 'user_name')
    autocomplete_fields = ('location', 'auth_user')
    readonly_fields = ['img_preview']
    list_per_page = 15


@admin.register(Goal)
class GoalsAdmin(admin.ModelAdmin):
    list_display = ("user", 'title', 'description',)
    search_fields = ('user', 'title')
    autocomplete_fields = ('user',)
    list_per_page = 15

# Test2


@admin.register(CurrentProgress)
class CurrentProgressAdmin(admin.ModelAdmin):
    list_display = ("user", 'name', 'description',)
    search_fields = ('user', 'name')
    autocomplete_fields = ('user',)
    list_per_page = 15


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'timestamp', 'referring_url')
    list_per_page = 15
