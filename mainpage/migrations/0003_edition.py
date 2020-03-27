# Generated by Django 3.0.4 on 2020-03-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20200321_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la edición')),
                ('active', models.BooleanField(default=True, help_text='Habilitar o deshabilitar esta edición')),
            ],
        ),
    ]