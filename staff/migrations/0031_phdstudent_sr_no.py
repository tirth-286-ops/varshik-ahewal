# Generated by Django 5.1 on 2025-03-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0030_teachingstaff_sr_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='phdstudent',
            name='sr_no',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
