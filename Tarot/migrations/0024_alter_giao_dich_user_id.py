# Generated by Django 4.2.1 on 2023-06-11 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tarot', '0023_alter_giao_dich_user_id_alter_giao_dich_user_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giao_dich',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
