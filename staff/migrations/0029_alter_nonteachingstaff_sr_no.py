# Generated by Django 5.1 on 2025-03-11 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0028_nonteachingstaff_sr_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonteachingstaff',
            name='sr_no',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
