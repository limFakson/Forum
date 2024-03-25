from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


from .forms import UserProfileForm, UserRegistrationForm
from .models import UserProfile, Videos, Posts


# Create your views here.
@login_required(login_url="/forum/login")
def home(request):
    userprofile = UserProfile.objects.get(user=request.user)
    post = Posts.objects.all()
    video = Videos.objects.all()
    return render(request,'Index.html',{'Home':'Title', 'Posts':post, 'Videos':video, 'userprofile':userprofile})

def createAccount(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile/onboarding   ')
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
                return redirect('user_profile_exists')
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
