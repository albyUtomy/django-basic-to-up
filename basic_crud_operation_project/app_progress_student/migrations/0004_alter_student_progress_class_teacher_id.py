# Generated by Django 5.1.2 on 2024-10-22 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_progress_student', '0003_student_progress_class_teacher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_progress',
            name='class_teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_progress_student.teacher'),
        ),
    ]
