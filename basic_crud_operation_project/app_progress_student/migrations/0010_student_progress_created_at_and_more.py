# Generated by Django 5.1.2 on 2024-10-24 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_progress_student', '0009_merge_20241023_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_progress',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 4, 9, 19, 953953, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='student_progress',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 4, 9, 20, 17702, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='teacher',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]