from django.contrib import admin
from .models import Post


@admin.register(Post)  # Rejestracja modelu za pomocą dekoratora @admin
class PostAdmin(admin.ModelAdmin):
    # Wyświetlanie pól na liście postów
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # Pasek boczny z filtracją
    list_filter = ('status', 'created', 'publish', 'author')
    # Pasek Search
    search_fields = ('title', 'body')
    # Automatyczne wypełnianie pola 'slug' na podstawie danych z 'title'
    prepopulated_fields = {'slug': ('title',)}
    # Widget wyszukiwania zamiast listy rozwijanej
    raw_id_fields = ('author',)
    # Linki nawigacyjne po datach
    date_hierarchy = 'publish'
    # Narzucenie sposobu sortowania
    ordering = ('status', 'publish')
