from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required

#Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

#Import Profile and UserDetails
from .models import Profile  # Import Profile model
#from .forms import UserDetailsForm  

def homepage(request):
    return render(request, 'mainpages/homepage.html')

def landingpage(request):
    return render(request, 'mainpages/landingpage.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("User successfully saved")
            return redirect("registration_success")
        else:
            print(form.errors)  # Print errors to debug validation issues

    context = {'registerform': form}
    return render(request, 'registration_login/register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("homepage")
    context = {'loginform':form}
    return render(request, 'registration_login/my_login.html',context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("landingpage")

def registration_success(request):
    return render(request, 'registration_login/registration_success.html')

def set_appointment(request):
    # Add your appointment logic here
    return render(request, 'appointments/set_appointment.html')


#@login_required(login_url="my_login")
#def profile(request):
    return render(request, 'registration_login/profile.html')

#@login_required(login_url="my_login")
#def user_details(request):
    user = request.user
    # Get the user's profile, or create it if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=user)
    
    if request.method == "POST":
        form = UserDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save(user=user)
            return redirect('profile')
    else:
        form = UserDetailsForm(instance=profile, initial={'first_name': user.first_name, 'last_name': user.last_name})
    
    context = {'form': form}
    return render(request, 'accounts/user_details.html', context)






