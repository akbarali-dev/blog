from django.contrib import admin

from about.models import Education, Testimonials

admin.site.register(Education)


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("full_name", 'description', 'img_preview')
    readonly_fields = ['img_preview']
