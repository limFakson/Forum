from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile, Videos, Posts


# Create your views here.
def home(request):
    post = Posts.objects.all()
    video = Videos.objects.all()
    return render(request,'Index.html',{'Home':'Title',
                                        'Posts':post,
                                        'Videos':video,})

def createAccount(request):
    if request.method == 'POST':
        username = request.POST.get("username", "default value")
        email = request.POST.get("email", "default value")
        password = request.POST.get("password", "default value").strip()
        password2 = request.POST.get("password2", "default value").strip()  # Fix typo here
        
        if password == password2:
            if User.objects.filter(username=username).exists():  
                messages.info(request, 'Username already exists')  
                return redirect('createAccount')
            
            elif User.objects.filter(email=email).exists():  
                messages.info(request, 'Email Already Used')
                return redirect('createAccount')

            else:
                user = User.objects.create_user(username=username, email=email, password=password2)  
                user.save()
                return redirect('create_profile')
        else:
            messages.info(request, 'Passwords do not match')  
            return redirect('createAccount')
    else:
        return render(request, 'createAccount.html', {'signUp': 'Title'})

def create_profile(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                # Associate the UserProfile instance with the authenticated user
                profile = form.save(commit=False)
                profile.user = request.user  # Set the user field to the authenticated user
                profile.save()  # Now commit the profile to the database
                messages.success(request, 'Your profile has been created successfully!')
                return redirect('/')
            else:
                messages.error(request, 'There was an error creating your profile. Please check the form.')
        else:
            return redirect('login')  # Redirect to login page if user is not authenticated
    else:
        form = UserProfileForm()
    return render(request, 'profilecreation.html', {'form': form, 'createProfile': 'Title'})




def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            # Check if the user has a profile
            if UserProfile.objects.filter(user=user).exists():
                return redirect('/')  # Redirect to homepage
            else:
                return redirect('create_profile')  # Redirect to profile creation page
            
        else:
            messages.error(request, "Invalid credentials")
            return redirect("Login")
    else:
        return render(request, "login.html", {'title': 'Login'})  
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    return render(request,'profile.html',{'Profile':'Title'})     