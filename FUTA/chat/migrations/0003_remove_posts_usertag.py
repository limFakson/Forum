# Generated by Django 5.0.2 on 2024-03-18 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_videos_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='usertag',
        ),
    ]
