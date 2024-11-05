from django.urls import path
from . import views
from .views import update_profile

app_name = 'userprofile'

urlpatterns = [
    path('profile/<str:username>/', views.view_profile, name='view_profile'),
    path('profile/update/<str:username>/', views.update_profile, name='update_profile'),
    path('profile/updatephoto/<str:username>/', views.update_photo, name='update_photo'),
]
    