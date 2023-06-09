# Generated by Django 4.2.1 on 2023-06-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarot', '0012_alter_user_cover_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default_avatar.jpg', null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_page',
            field=models.ImageField(blank=True, default='cover_pages/banner.jpg', null=True, upload_to='cover_pages/'),
        ),
    ]