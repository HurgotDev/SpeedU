# Generated by Django 3.0.4 on 2020-03-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configmainpagemodel',
            name='logo',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]