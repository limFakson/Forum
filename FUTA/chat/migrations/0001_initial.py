# Generated by Django 5.0.2 on 2024-03-18 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertag', models.CharField(max_length=10)),
                ('authordp', models.ImageField(blank=True, null=True, upload_to='static/media/images/')),
                ('content', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media/images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authordp', models.ImageField(blank=True, null=True, upload_to='static/media/images/')),
                ('content', models.CharField(max_length=50)),
                ('video', models.ImageField(blank=True, null=True, upload_to='static/media/videos/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]