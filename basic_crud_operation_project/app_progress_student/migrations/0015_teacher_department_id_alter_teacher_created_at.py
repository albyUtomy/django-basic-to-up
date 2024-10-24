# Generated by Django 5.1.2 on 2024-10-24 05:58

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0005_alter_department_created_at'),
        ('app_progress_student', '0014_alter_teacher_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='department_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='teachers', to='app_department.department'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 5, 58, 19, 476811, tzinfo=datetime.timezone.utc)),
        ),
    ]
