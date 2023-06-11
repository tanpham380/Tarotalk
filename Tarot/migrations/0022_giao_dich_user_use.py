# Generated by Django 4.2.1 on 2023-06-11 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tarot', '0021_rename_dich_vu_giao_dich'),
    ]

    operations = [
        migrations.AddField(
            model_name='giao_dich',
            name='user_use',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_use', to=settings.AUTH_USER_MODEL),
        ),
    ]