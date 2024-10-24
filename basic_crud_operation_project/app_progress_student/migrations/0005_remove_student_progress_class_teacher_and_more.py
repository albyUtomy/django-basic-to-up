# Generated by Django 5.1.2 on 2024-10-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_progress_student', '0004_alter_student_progress_class_teacher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_progress',
            name='class_teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='performance_rate',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
    ]