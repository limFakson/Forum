from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Index.html',{'Home':'Title'})
def profile(request):
    return render(request,'profile.html',{'Profile':'Title'})
def login(request):
    return render(request,'login.html',{'Login':'Title'})
def createAccount(request):
    return render(request,'createAccount.html',{'signUp':'Title'})