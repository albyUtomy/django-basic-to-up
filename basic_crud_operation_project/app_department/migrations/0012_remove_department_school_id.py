# Generated by Django 5.1.2 on 2024-10-30 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0011_alter_department_department_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='school_id',
        ),
    ]
