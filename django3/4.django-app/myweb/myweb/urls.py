
from django.contrib import admin
from django.urls import path

from . import views
from blog import views as blogviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/',blogviews.index)
]
