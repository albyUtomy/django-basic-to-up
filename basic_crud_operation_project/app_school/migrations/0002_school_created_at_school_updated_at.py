# Generated by Django 5.1.2 on 2024-10-24 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 4, 48, 59, 344089, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='school',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
