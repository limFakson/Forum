from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Index.html',{'Home':'Title'})


def profile(request):
    return render(request,'profile.html',{'profile':'Title'})