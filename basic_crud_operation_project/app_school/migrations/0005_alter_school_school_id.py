# Generated by Django 5.1.2 on 2024-10-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_school', '0004_alter_school_school_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_id',
            field=models.IntegerField(default=100, editable=False, primary_key=True, serialize=False),
        ),
    ]
