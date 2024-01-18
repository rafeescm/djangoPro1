from django.shortcuts import render, redirect
from .models import MovieInfo
from django.http import HttpResponse
from .forms import MovieInfoForm


# Create your views here.
def create(request):

    if request.method == "POST":
        form = MovieInfoForm(request.POST,request.FILES)
        # title = request.POST.get("title")
        # year = request.POST.get("year")
        # summary = request.POST.get("summary")
        # movie_obj = MovieInfo(title=title, year=year, summary=summary)
        if form.is_valid():
            form.save()
        print(request.POST)
        print(request.POST.get("summary"))
    else:
        form = MovieInfoForm()
    return render(request, "firstApp/create.html",{"form":form})


def list(request):
    movie_details = MovieInfo.objects.all()
    print(movie_details)
    return render(request, "firstApp/list.html", {"movies":movie_details})


def edit(request,pk):
    edit_obj = MovieInfo.objects.get(id=pk)
    if request.method == "POST":
        frm = MovieInfoForm(request.POST,instance=edit_obj)
        if frm.is_valid():
            frm.save()
        # title = request.POST.get("title")
        # year = request.POST.get("year")
        # summary = request.POST.get("summary")
        # edit_obj.title = title
        # edit_obj.year = year
        # edit_obj.summary = summary
        # edit_obj.save()
        return redirect("firstApp:list")
    else:
        form = MovieInfoForm(instance=edit_obj)
    # return render(request, "firstApp/edit.html",{"edit_item":edit_obj})
    return render(request, "firstApp/create.html", {"form": form})
def delete(request,pk):
    del_obj = MovieInfo.objects.get(id=pk)
    del_obj.delete()
    movie_details = MovieInfo.objects.all()
    print(movie_details)
    return render(request, "firstApp/list.html", {"movies": movie_details})
