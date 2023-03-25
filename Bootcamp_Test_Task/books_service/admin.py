from django.contrib import admin
from .models import Author, Genre, Book, Language

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - filters that will be displayed in sidebar (list_filter)
    """
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    list_filter = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('title', 'display_author', 'display_genre')
    fieldsets = (
        (None, {
            'fields': ('title','author')
        }),
        ('Description', {
            'fields': ('summary', 'isbn', 'genre', 'language')
        }),
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)