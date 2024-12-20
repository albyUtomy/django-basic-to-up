# Generated by Django 5.1.2 on 2024-10-26 05:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0005_alter_department_hod_name_alter_department_school_id'),
        ('app_teacher', '0006_rename_employee_id_teacher_teacher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='hod_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='app_teacher.teacher', unique=True),
        ),
    ]
