# Generated by Django 5.1.2 on 2024-10-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_progress_student', '0004_remove_student_progress_total_mark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_progress',
            name='roll_no',
            field=models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
    ]