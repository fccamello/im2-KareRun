from django.urls import path
from . import views

urlpatterns = [
    path('appeal/',views.appeal,name="appeal"),
    path('appealList/',views.appealList,name="appealList"),
]

