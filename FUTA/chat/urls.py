from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='Homepage'),
    path('createAccount', views.createAccount, name= 'createAccount'),
    path('login', views.login, name= 'Login'),
    path('logout', views.login, name = 'logout'),
    path('profile', views.profile, name= 'profilePage'),
]
