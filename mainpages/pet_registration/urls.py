from django.urls import path
from . import views

urlpatterns = [
    path('register_pet/', views.pet_registration, name='register_pet'),
    path('pet_registration_success/<str:pet_id>/', views.pet_registration_success, name='pet_registration_success'),
    path('profile/<str:pet_id>/', views.pet_profile, name='pet_profile'),
]
