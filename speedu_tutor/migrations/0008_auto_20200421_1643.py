# Generated by Django 3.0.4 on 2020-04-21 21:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('speedu_tutor', '0007_auto_20200421_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cc',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='doc_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='doc_type',
            field=models.CharField(choices=[('CC', 'Cédula de ciudadania'), ('TI', 'Tarjeta de identidad')], default='CC', max_length=2),
            preserve_default=False,
        ),
    ]