from django.contrib import admin
from .models import Posts, UserProfile
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')

admin.site.register(UserProfile)
admin.site.register(Posts, PostsAdmin)