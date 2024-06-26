from django.contrib.auth.models import User
from django.db import models


faculty_choices = [
        ('SOS', 'School of Science'),
        ('SOC', 'School of Computing'),
        ('SEET', 'School of Engineering and Engineering Technology'),
        ('SAAT', 'School of Agriculture and Agriculture Technology'),
        ('SLIT', 'School of Logistics and Innovative Technology'),
        ('SHHT', 'School of Health  and Health Technology'),
        ('SEMS', 'School of Earth and Mineral Sciences'),
        ('SET', 'School of Environmental Technology'),
    ]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    matricNumber = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100, choices=faculty_choices)
    profile_picture = models.ImageField(upload_to='files/profiles/')

    def __str__(self):
        return self.user.username

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='files/post/image', null=True, blank=True)
    docm = models.FileField(upload_to='files/post/docs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
