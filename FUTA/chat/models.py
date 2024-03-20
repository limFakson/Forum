from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    matricNumber = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    faculty_choices = [
        ('Science', 'School of Science'),
        ('Computing', 'School of Computing'),
        ('Engineering', 'School of Engineering'),
        ('Agriculture', 'School of Agriculture'),
        ('Management', 'School of Management Technology'),
        ('Health', 'School of Health'),
        ('Earth', 'School of Earth and Mineral Sciences'),
        ('Postgraduate', 'School of Postgraduate Studies'),
        ('Predegree', 'School of Predegree Studies'),
        ('Environmental', 'School of Environmental Technology'),
    ]
    faculty = models.CharField(max_length=100, choices=faculty_choices)    
    profile_picture = models.ImageField(upload_to='profiles/', default='default.jpg')

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    image = models.FileField(upload_to='static/media/images/', null=True, blank=True)

class Videos(models.Model):
    authordp = models.ImageField(upload_to='static/media/images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.CharField(max_length=50)
    video = models.FileField(upload_to='static/media/videos/', null=True, blank=True, default='static/media/videos/Numbbug.mp4')
