from django.contrib import admin
from .models import  MovieInfo
# Register your models here.
class MoviesInfoAdmin(admin.ModelAdmin):
    list_display = ["title","year"]
admin.site.register(MovieInfo,MoviesInfoAdmin)

