"""
URL configuration for mainpages project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appointments import views as appointments_views
from landingpage import views as landing_views
from registration_login import views as registration_views
from homepage import views as homepage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_views.homepage, name='homepage'),

    # Appointment URLs
    path('appointments/', appointments_views.appointments_page, name="appointments_page"),
    path('set-appointment/', appointments_views.set_appointment, name='set_appointment'),
    path('appointments/cancel/<int:id>/', appointments_views.cancel_appointment, name='cancel_appointment'),  

    # Landing page
    path('landingpage/', landing_views.landingpage, name='landingpage'),

    # Authentication
    path('login/', registration_views.my_login, name='my_login'),
    path('logout/', registration_views.user_logout, name='logout'),
    path('register/', registration_views.register, name='register'),
    path('registration_success/', registration_views.registration_success, name='registration_success'),

    # Profile and other apps
    # path('profile/', registration_views.profile, name='profile'),
    path('pet_registration/', include('pet_registration.urls')),
]
