from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    return render(request,"firstApp/create.html")

def list(request):
    return render(request,"firstApp/list.html")

def edit(request):
    return render(request,"firstApp/edit.html")