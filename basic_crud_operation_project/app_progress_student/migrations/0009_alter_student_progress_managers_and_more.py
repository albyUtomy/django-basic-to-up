# Generated by Django 5.1.2 on 2024-11-04 04:32

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_progress_student', '0008_alter_student_progress_roll_no'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student_progress',
            managers=[
                ('active_object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='student_progress',
            name='chemistry_mark',
        ),
        migrations.RemoveField(
            model_name='student_progress',
            name='maths_mark',
        ),
        migrations.RemoveField(
            model_name='student_progress',
            name='physics_mark',
        ),
    ]
