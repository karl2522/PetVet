from django.urls import path
from . import views

urlpatterns = [
    path('register_pet/', views.pet_registration, name='register_pet'),
    path('pet_registration_success/<str:pet_id>/', views.pet_registration_success, name='pet_registration_success'),
    path('profile/<str:pet_id>/', views.pet_profile, name='pet_profile'),
    path('profile/<str:pet_id>/update/', views.update_pet, name='update_pet'),  
     # New URL pattern for listing pets by owner
    path('pets/', views.pet_list_by_owner, name='pet_list_by_owner'),
    path('delete/<str:pet_id>/', views.delete_pet, name='delete_pet'),  
]
