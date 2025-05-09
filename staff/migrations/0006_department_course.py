# Generated by Django 5.1 on 2025-02-17 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_examresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('boys_general', models.PositiveIntegerField(default=0)),
                ('boys_st', models.PositiveIntegerField(default=0)),
                ('boys_sc', models.PositiveIntegerField(default=0)),
                ('boys_sebc', models.PositiveIntegerField(default=0)),
                ('boys_ews', models.PositiveIntegerField(default=0)),
                ('girls_general', models.PositiveIntegerField(default=0)),
                ('girls_st', models.PositiveIntegerField(default=0)),
                ('girls_sc', models.PositiveIntegerField(default=0)),
                ('girls_sebc', models.PositiveIntegerField(default=0)),
                ('girls_ews', models.PositiveIntegerField(default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='staff.department')),
            ],
        ),
    ]
