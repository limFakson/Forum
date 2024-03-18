from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Posts
from .models import Videos


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
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')  
            return redirect('createAccount')
    else:
        return render(request, 'createAccount.html', {'signUp': 'Title'})
   

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "default value")
        password = request.POST.get("password2", "default value")
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
            
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request,"login.html",{'Login':'Title'})    
    
def profile(request):
    return render(request,'profile.html',{'Profile':'Title'})     