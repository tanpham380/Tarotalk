# Generated by Django 4.2.1 on 2023-05-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarot', '0003_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
