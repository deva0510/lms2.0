# Generated by Django 4.2.4 on 2024-04-24 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0206_remove_zoommeeting_meeting_time_zoommeeting_endtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeloginlogout',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 10, 27, 42, 577621)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 10, 27, 42, 644031)),
        ),
        migrations.AlterField(
            model_name='shift_names',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 24, 10, 27, 42, 574007)),
        ),
        migrations.AlterField(
            model_name='shift_names',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 24, 10, 27, 42, 574007)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 24, 10, 27, 42, 593264)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 24, 10, 27, 42, 593264)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 24, 10, 27, 42, 593264)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 24, 10, 27, 42, 593264)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 4, 24, 10, 27, 42, 591413)),
        ),
    ]
