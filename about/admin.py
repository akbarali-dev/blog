from django.contrib import admin

from about.models import *

admin.site.register([Education, SocialNetwork, Icon, Contact])


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("full_name", 'description', 'img_preview')
    readonly_fields = ['img_preview']


@admin.register(Client)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'description', 'img_preview')
    readonly_fields = ['img_preview']
