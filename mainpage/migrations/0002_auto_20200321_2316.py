# Generated by Django 3.0.4 on 2020-03-22 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='departament',
            options={'ordering': ['name']},
        ),
    ]
