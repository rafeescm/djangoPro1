from  django.urls import path
from . import views

app_name = "firstApp"
urlpatterns = [
    path('create',views.create,name="create"),
    path('edit/<pk>',views.edit,name="edit"),
    path('',views.list,name="list"),
    path('delete/<pk>',views.delete,name="delete"),
]