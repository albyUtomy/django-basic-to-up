# Generated by Django 5.1.2 on 2024-10-25 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0003_alter_department_hod_name_alter_department_school_id'),
        ('app_progress_student', '0001_initial'),
        ('app_school', '0002_rename_principle_name_school_principal_name'),
        ('app_teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_progress',
            name='class_teacher_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_teacher.teacher'),
        ),
        migrations.AlterField(
            model_name='student_progress',
            name='department_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='app_department.department'),
        ),
        migrations.AlterField(
            model_name='student_progress',
            name='school_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='app_school.school'),
        ),
    ]