# Generated by Django 3.0.4 on 2020-03-26 14:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('speedu_tutor', '0003_auto_20200326_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='hour_end',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
