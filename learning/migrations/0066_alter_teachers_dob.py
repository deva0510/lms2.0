# Generated by Django 4.2.3 on 2024-02-02 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0065_alter_teachers_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 14, 30, 4, 685167)),
        ),
    ]
