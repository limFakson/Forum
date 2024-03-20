from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Homepage'),
    path('home', views.home, name='Homepage'),
    path('forum/register', views.createAccount, name= 'createAccount'),
    path('create_profile', views.create_profile, name= 'create_profile'),
    path('forum/login', views.login, name= 'Login'),
    path('logout', views.logout, name = 'logout'),
    path('forum/profile', views.profile, name= 'profilePage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)