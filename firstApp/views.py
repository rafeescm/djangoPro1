from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_django(request):
    movie_details = {"movies":[{
        "title":"bigB",
        "year":2009,
        # "summary":"gangster story",
        "success":False,
    },
        {
            "title": "bigC",
            "year": 2010,
            "summary": "Love story",
            "success": True,
        },
        {
            "title": "bigD",
            "year": 2011,
            "summary": "Happy story",
            "success": True,
        },
    ]}
    return render(request,'firstApp/base.html',movie_details)

