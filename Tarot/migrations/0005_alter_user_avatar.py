# Generated by Django 4.2.1 on 2023-05-31 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarot', '0004_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='static/img/avatars/default_avatar.jpg', null=True, upload_to='static/avatars/'),
        ),
    ]