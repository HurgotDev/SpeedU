# Generated by Django 3.0.4 on 2020-04-08 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speedu_tutor', '0004_schedule_hour_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='institution_type',
        ),
    ]
