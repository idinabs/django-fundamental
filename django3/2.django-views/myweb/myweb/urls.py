

from django.contrib import admin
from django.urls import path

# import views/meresponse menggunakan file views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index)
]
