from django.contrib import admin
from movies.models import Category, MovieType, Movie

# Register model Category to show for admin panel
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "movie_type", )


@admin.register(MovieType)
class MovieTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug",)