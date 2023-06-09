# Generated by Django 4.2.1 on 2023-06-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarot', '0008_alter_user_avatar_alter_user_cover_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='static/img/avatars/default_avatar.jpg', null=True, upload_to='static/avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_page',
            field=models.ImageField(blank=True, null=True, upload_to='static/cover_pages/'),
        ),
    ]