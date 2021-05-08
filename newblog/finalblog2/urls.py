from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', blogsub2, name="blogsub2"),
    path('blognew2/', blognew2, name="blognew2"),
    path('create2/', create2, name="create2"),
    path('edit2/<str:id>', edit2, name="edit2"),
    path('update2/<str:id>', update2, name="update2"),
    path('delete2/<str:id>', delete2, name="delete2"),
]