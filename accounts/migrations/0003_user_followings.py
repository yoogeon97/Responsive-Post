# Generated by Django 4.2.7 on 2023-11-10 02:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_profilr_image_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
