from  django.urls import path
from . import views

app_name = "firstApp"
urlpatterns = [
    path('create',views.create,name="create"),
    path('edit',views.edit,name="edit"),
    path('list',views.list,name="list"),
]