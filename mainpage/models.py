import os
from uuid import uuid4

from django.db import models
from django.utils import timezone


def path_and_rename(path, name=''):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        now = timezone.now()
        #get filename
        if name != '':
            filename = '{}_{}.{}'.format(name,now, ext)
        else:
            #set filename as random string
            filename = '{}_{}.{}'.format(uuid4().hex, now, ext)
        return os.path.join(path, filename)
    return wrapper


class Edition(models.Model):
    name = models.CharField('Nombre de la edición', max_length=100, unique=True)
    active = models.BooleanField(default=True, help_text='Habilitar o deshabilitar esta edición')

    def __str__(self):
        return self.name

# Models to localities

class Country(models.Model):
    name = models.CharField('Nombre del país', max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Departament(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField('Nombre del departamento', max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class City(models.Model):
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    name = models.CharField('Nombre de la ciudad', max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Register(models.Model):
    institution = models.CharField(max_length=255, help_text='Nombre de la institución')
    name = models.CharField(max_length=100, help_text='Nombres del representante')
    lastname = models.CharField(max_length=100, help_text='Apellidos del representante')
    email = models.CharField(max_length=100, help_text='Correo de contacto')
    phone = models.IntegerField(help_text='Teléfono de contacto')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)

class Newsletter(models.Model):
    email = models.CharField(max_length=100, unique=True, help_text='Correo suscrito al boletín informativo')
    active = models.BooleanField(default=True, help_text='Si si establece en True se enviaran noticas del boletín...')

    def __str__(self):
        return self.email


