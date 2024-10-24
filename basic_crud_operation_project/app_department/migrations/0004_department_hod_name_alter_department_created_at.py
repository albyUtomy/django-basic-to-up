# Generated by Django 5.1.2 on 2024-10-24 05:50

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0003_remove_department_hod_name_department_created_at_and_more'),
        ('app_progress_student', '0014_alter_teacher_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='hod_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='departments', to='app_progress_student.teacher'),
        ),
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 5, 50, 34, 235657, tzinfo=datetime.timezone.utc)),
        ),
    ]