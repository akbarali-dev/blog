from django.contrib import admin

from about.models import *


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'start_year', 'graduation_year')
    search_fields = ("name",)
    autocomplete_fields = ("user",)
    # list_select_related = ("user", )


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'link')
    list_filter = ('name',)
    search_fields = ("name",)
    autocomplete_fields = ('icon', 'user',)


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    search_help_text = 'name'
    search_fields = ('name',)
    list_per_page = 15


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("full_name", 'description', 'img_preview')
    readonly_fields = ['img_preview']
    autocomplete_fields = ("user",)
    search_fields = ('full_name',)
    list_per_page = 15


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("user", "name", 'description', 'img_preview')
    search_fields = ('name',)
    autocomplete_fields = ("user",)
    readonly_fields = ['img_preview']
    list_per_page = 15


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", 'email', 'description')
    search_fields = ("full_name", 'email',)
    autocomplete_fields = ("user",)
    list_per_page = 15


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)
    list_per_page = 15


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('data',)
    search_fields = ('data',)
