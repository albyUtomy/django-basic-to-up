# Generated by Django 5.1.2 on 2024-10-18 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_progress_student', '0002_student_progress_gained_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_progress',
            name='gained_mark',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
    ]
