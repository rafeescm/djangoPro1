from django.contrib import admin
from .models import  MovieInfo,Director,CensorInfo,Actor
class MoviesInfoAdmin(admin.ModelAdmin):
    list_display = ["title","year"]
admin.site.register(MovieInfo,MoviesInfoAdmin)
admin.site.register(Director)
admin.site.register(CensorInfo)
admin.site.register(Actor)

