# Generated by Django 5.1.2 on 2024-10-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_progress_student', '0005_remove_student_progress_class_teacher'),
    ]
    

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='performance_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
