# Generated by Django 5.1.2 on 2024-10-24 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_school', '0010_alter_school_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 5, 31, 51, 275093, tzinfo=datetime.timezone.utc)),
        ),
    ]
