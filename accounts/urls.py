from django.urls import path
from .views import signup_view, login_view
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect

urlpatterns = [
    
    path('', lambda request: HttpResponseRedirect('signup/')),  # Redirects /accounts to /accounts/signup/
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
