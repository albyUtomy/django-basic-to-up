# Generated by Django 5.1.2 on 2024-10-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_department', '0008_department_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
