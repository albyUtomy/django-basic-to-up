# Generated by Django 5.1.2 on 2024-10-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0007_alter_department_hod_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]