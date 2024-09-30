from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name="Register"),
    path('sucess',views.success,name="sucess")
]
