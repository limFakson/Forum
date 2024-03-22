from django.contrib import admin
from .models import Posts, Videos, UserProfile
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Posts)
admin.site.register(Videos)