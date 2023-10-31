from django.contrib import admin

from programming.models import Skills, Category, Portfolio, Experience, Technology


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("name", 'discount', 'technology',)
    search_fields = ("name", 'technology',)
    autocomplete_fields = ('technology',)
    list_per_page = 15


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('user', "name", 'discount',)
    search_fields = ("name", 'user',)
    autocomplete_fields = ('user',)
    list_per_page = 15


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_per_page = 15


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', "name", 'description', 'get_category', 'img_preview')
    search_fields = ("name", 'user',)
    autocomplete_fields = ('user',)
    readonly_fields = ['img_preview']
    list_per_page = 15

    def get_category(self, obj):
        return ", n".join([c.name for c in obj.category.all()])


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', "name", 'start_year', 'graduation_year', 'description',)
    autocomplete_fields = ('user',)
    search_fields = ("name", 'user', 'start_year', 'graduation_year',)
