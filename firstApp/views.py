from django.shortcuts import render
from .models import MovieInfo
from django.http import HttpResponse
from .forms import MovieInfoForm


# Create your views here.
def create(request):
    form = MovieInfoForm()
    if request.method == "POST":
        form = MovieInfoForm(request.POST)
        # title = request.POST.get("title")
        # year = request.POST.get("year")
        # summary = request.POST.get("summary")
        # movie_obj = MovieInfo(title=title, year=year, summary=summary)
        if form.is_valid():
            form.save()
        print(request.POST)
        print(request.POST.get("summary"))
    return render(request, "firstApp/create.html",{"form":form})


def list(request):
    movie_details = MovieInfo.objects.all()
    print(movie_details)
    return render(request, "firstApp/list.html", {"movies":movie_details})


def edit(request):
    return render(request, "firstApp/edit.html")
