from django.contrib import admin
from .models import Categories, Articles


# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    list_display=("name",)
    list_filter=("created", "updated")


class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    list_display=("title", 'subtitle', "author")
    list_filter=("created", "updated")


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)

