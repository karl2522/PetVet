from django.urls import path
from . import views

urlpatterns = [
    path('overview/<int:owner_id>/', views.billing_overview, name='billing_overview'),  # Existing URL
    path('add_payment/', views.add_payment, name='add_payment'),  # New URL for adding payment
]
