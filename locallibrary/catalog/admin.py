from django.contrib import admin
from .models import Author, Genre, Language, Book, BookInstance


# Register your models here.


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookInstance)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# @admin.register(Book) class BookAdmin ... === admin.site.register(Book, BookAdmin)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre')
    list_filter = ('author', 'genre', 'language')

    inlines = [BooksInstanceInline]
