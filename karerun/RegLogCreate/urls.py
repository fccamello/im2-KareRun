from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('register/sucess/',views.success,name="sucess"),
    path('login/',views.login,name="login"),
]
