from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category)
class CatergoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
