from django.shortcuts import render
from .models import MovieInfo
from django.http import HttpResponse


# Create your views here.
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        summary = request.POST.get("summary")
        movie_obj = MovieInfo(title=title, year=year, summary=summary)
        movie_obj.save()
        print(request.POST)
        print(request.POST.get("summary"))
    return render(request, "firstApp/create.html")


def list(request):
    movie_details = MovieInfo.objects.all()
    print(movie_details)
    return render(request, "firstApp/list.html", {"movies":movie_details})


def edit(request):
    return render(request, "firstApp/edit.html")
