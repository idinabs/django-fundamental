
from django.contrib import admin
from django.urls import path

# url tanpa views.py

from django.http import HttpResponse

def index(request):
	return HttpResponse("hello world")

def about(request):
	return HttpResponse("ini adalah about")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/',about) 
]
