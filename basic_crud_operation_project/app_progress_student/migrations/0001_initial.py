# Generated by Django 5.1.2 on 2024-10-21 15:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Progress',
            fields=[
                ('roll_no', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('chemistry_mark', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('physics_mark', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('maths_mark', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('out_off', models.IntegerField(blank=True, default=300, editable=False, null=True)),
                ('gained_mark', models.FloatField(blank=True, editable=False, null=True)),
                ('class_teacher', models.CharField(max_length=50)),
                ('percentage', models.FloatField(blank=True, editable=False, null=True)),
            ],
        ),
    ]
