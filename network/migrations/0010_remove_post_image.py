# Generated by Django 4.2.5 on 2023-10-24 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_remove_user_profile_picture_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]