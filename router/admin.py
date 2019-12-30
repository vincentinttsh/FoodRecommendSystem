from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'address']
    list_filter = ['category']
    ordering = ['category']
    search_fields = ['name', 'address', 'description']
    list_per_page = 20


@admin.register(CommentField)
class CommentFieldAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'name', 'grade']
    list_filter = ['grade']
    ordering = ['restaurant', 'grade', 'name']
    search_fields = ['name', 'comment', 'restaurant']


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'restaurant', 'handle']
    list_filter = ['category', 'handle']
    ordering = ['restaurant', 'category', 'handle']
    search_fields = ['name', 'email', 'restaurant']
