# Generated by Django 4.2.1 on 2023-06-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarot', '0026_remove_giao_dich_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giao_dich',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
