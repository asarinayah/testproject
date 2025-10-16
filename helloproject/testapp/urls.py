# greeting/urls.py

from django.urls import path
from . import views  # This imports your local views.py file

urlpatterns = [
    path('', views.hello, name='hello'),
]