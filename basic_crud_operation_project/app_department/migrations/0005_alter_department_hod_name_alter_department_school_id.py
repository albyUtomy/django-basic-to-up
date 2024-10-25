# Generated by Django 5.1.2 on 2024-10-25 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0004_alter_department_hod_name_alter_department_school_id'),
        ('app_school', '0002_rename_principle_name_school_principal_name'),
        ('app_teacher', '0004_alter_teacher_school_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='hod_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='app_teacher.teacher'),
        ),
        migrations.AlterField(
            model_name='department',
            name='school_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_department', to='app_school.school'),
        ),
    ]