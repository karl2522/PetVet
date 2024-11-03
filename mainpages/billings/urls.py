from django.urls import path
from . import views

app_name = 'billings'

urlpatterns = [
    path('overview/<int:owner_id>/', views.billing_overview, name='billing_overview'),
    path('add_payment/', views.add_payment, name='add_payment'),
    path('choose-payment/', views.choose_payment_method, name='choose_payment_method'),
    path('manage_billing/', views.manage_billing, name='manage_billing'),
]
