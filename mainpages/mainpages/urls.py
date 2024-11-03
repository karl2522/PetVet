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
from billings import views   

app_name = 'billings'

urlpatterns = [
    path('admin/', admin.site.urls),
    ##path('', views.homepage, name='homepage'),
    ##path('set-appointment/', views.set_appointment, name='set_appointment'),
    path('billing/', include('billings.urls', namespace='billings')),
    path('update_billing/<int:billing_id>/', views.update_billing, name='update_billing'),
    path('delete_billing/<int:billing_id>/', views.delete_billing, name='delete_billing'),
]
