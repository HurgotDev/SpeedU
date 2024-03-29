# Generated by Django 3.0.4 on 2020-03-22 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre del país')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='Correo suscrito al boletín informativo', max_length=100, unique=True)),
                ('active', models.BooleanField(default=True, help_text='Si si establece en True se enviaran noticas del boletín...')),
            ],
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre del departamento')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la ciudad')),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Departament')),
            ],
        ),
    ]
