from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("summary"))
    return render(request,"firstApp/create.html")

def list(request):
    movie_details = {"movies": [{
        "title": "bigB",
        "year": 2009,
        # "summary":"gangster story",
        "success": False,
        "img":"bigb.jpg",
    },
        {
            "title": "bigC",
            "year": 2010,
            "summary": "Love story",
            "success": True,
            "img":"images2.jpeg"
        },
        {
            "title": "bigD",
            "year": 2011,
            "summary": "Happy story",
            "success": True,
            "img" :"image3.jpg"
        },
    ]}
    return render(request,"firstApp/list.html",movie_details)

def edit(request):
    return render(request,"firstApp/edit.html")