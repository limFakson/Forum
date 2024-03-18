from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    authordp = models.ImageField(upload_to='static/media/images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length= 200)
    image = models.ImageField(upload_to='static/media/images/', null=True, blank=True)

class Videos(models.Model):
    authordp = models.ImageField(upload_to='static/media/images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.CharField(max_length = 50)
    video = models.FileField(upload_to='static/media/videos/', null=True, blank=True, default= 'static/media/videos/Numbbug.mp4')