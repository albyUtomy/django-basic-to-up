# Generated by Django 5.1.2 on 2024-10-25 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_department', '0001_initial'),
        ('app_school', '0001_initial'),
        ('app_teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='hod_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='departments', to='app_teacher.teacher'),
        ),
        migrations.AddField(
            model_name='department',
            name='school_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='school_department', to='app_school.school'),
        ),
    ]
