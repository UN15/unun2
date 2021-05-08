from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', blogsub, name="blogsub"),
    path('blognew/', blognew, name="blognew"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name= "delete"),
]