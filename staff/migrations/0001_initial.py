# Generated by Django 5.1 on 2025-02-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NonTeachingStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=255)),
                ('class1_female', models.IntegerField(default=0)),
                ('class1_male', models.IntegerField(default=0)),
                ('class2_female', models.IntegerField(default=0)),
                ('class2_male', models.IntegerField(default=0)),
                ('class3_female', models.IntegerField(default=0)),
                ('class3_male', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
    ]
