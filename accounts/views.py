from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # This logs in the user
            return redirect('profile')  # Redirect after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method=="POST":
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('profile')
        
    else:
        form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def profile(request):
    return render(request,'accounts/profile.html')