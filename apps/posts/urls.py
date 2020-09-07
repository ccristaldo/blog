from django.contrib import admin
from django.urls import path
from . import views

app_name="posts"

urlpatterns = [
    path('', views.Posts_list, name = "Posts")
]
