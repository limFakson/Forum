from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from .forms import UserProfileForm, UserRegistrationForm, UserPosts
from .models import UserProfile, Posts


# Create your views here.
@login_required(login_url="/forum/login")
def home(request):
    if request.method == 'POST':
        form = UserPosts(request.POST)

    userprofile = UserProfile.objects.get(user=request.user)
    post = Posts.objects.all()
    return render(request,'Index.html',{
        'Home':'Title', 
        'Posts':post, 
        'userprofile':userprofile
        })

def createAccount(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile/onboarding')
        else:
            return render(request, 'registration/createAccount.html', {'form': form, 'signUp': 'Title'})
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/createAccount.html', {'form': form, 'signUp': 'Title'})

@login_required(login_url="/forum/login")
def create_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            if not hasattr(request.user, 'userprofile'):
                form.save()
                return redirect('/home')
            else:
                form.save()
                return redirect('/home')
        else:
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

    else:        
        form = UserProfileForm(instance=user_profile)

    return render(request, 'registration/profilecreation.html', {'form': form, 'createProfile': 'Title'})

   
def logout_view(request):
    logout(request)
    return redirect('/home')


def profile(request):
    return render(request,'profile.html',{'Profile':'Title'})    
