# Generated by Django 5.1 on 2025-02-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_examresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ક્રમ', models.IntegerField()),
                ('શિક્ષકનું_નામ_અને_હોદ્દો', models.CharField(max_length=255)),
                ('કોન્ફરન્સ_પરિસંવાદ_કાર્યશાળા', models.CharField(max_length=255)),
                ('સ્થાન_અને_તારીખ', models.CharField(max_length=255)),
                ('રજુ_કરેલા_અભ્યાસ_લેખનું_શીર્ષક', models.CharField(max_length=255)),
            ],
        ),
    ]
