from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,ProfileUpdateForm
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"{username} your account has been created and now you can login!")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return  render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_updateform = UserUpdateForm(request.POST,instance = request.user)
        p_updateform = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if u_updateform.is_valid() and p_updateform.is_valid():
            u_updateform.save()
            p_updateform.save()
            return redirect('profile')
    else:
        u_updateform = UserUpdateForm(instance=request.user)
        p_updateform = ProfileUpdateForm( instance=request.user.profile)

    context={
        'u_updateform':u_updateform,
        'p_updateform':p_updateform,
     }
    return render(request,'users/profile.html',context)