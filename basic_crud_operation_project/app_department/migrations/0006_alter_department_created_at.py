# Generated by Django 5.1.2 on 2024-10-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0005_alter_department_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
