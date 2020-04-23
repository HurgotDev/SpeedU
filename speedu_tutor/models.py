from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

import os
from uuid import uuid4

def wrapper(instance, filename):
    ext = filename.split('.')[-1]
    now = timezone.now()
    filename = '{}_{}.{}'.format(uuid4().hex, now, ext)           
    return os.path.join('images/institutions', filename)

class Institution(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=wrapper)

    def __str__(self):
        return self.name   
    

class Career(models.Model):
    name = models.CharField(max_length=100)
    institution = models.ManyToManyField(Institution)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ManyToManyField(Career)

    def __str__(self):
        return self.name

class Student(models.Model):

    CHOICES_DOC_TYPE = [
        ('CC', 'Cédula de ciudadania'),
        ('TI', 'Tarjeta de identidad'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=2, choices=CHOICES_DOC_TYPE)
    doc_number = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10, unique=True)
    semester = models.IntegerField()
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

class Tutor(models.Model):
    CHOICES_STATES = [
        ('V', 'En Verificación'),
        ('A', 'Aprobado'),
        ('R', 'Rechsazado'),
        ('I', 'Inactivo'),
    ]

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()
    argument = models.TextField()
    state = models.CharField(max_length=1, choices=CHOICES_STATES, default='En Verificación')

    def __str__(self):
        return '{} {}'.format(self.student.user.first_name, self.student.user.last_name)

class Schedule(models.Model):
    CHOICES_DAYS = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miercoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sabado'),
    ]
    
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=CHOICES_DAYS)
    hour_start = models.TimeField()
    hour_end = models.TimeField()

    def __str__(self):
        return '{} {}-{}'.format(self.day, self.hour_start, self.hour_end)

class Tutorial(models.Model):
    CHOICES_STATES = [
        ('0', 'Programada'),
        ('1', 'Termininada'),
    ]

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)   
    semester = models.IntegerField()
    state = models.CharField(max_length=1, choices=CHOICES_STATES, default='Programada')

    def __str__(self):
        return '{}-{} Semester {}'.format(self.schedule.hour_start, self.schedule.hour_end, self.semester)
    
    def get_absolute_url(self):
        return reverse('tutorial-detail', args=[str(self.id)])

class Competitor(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attended_tutor = models.BooleanField()
    attended_student = models.BooleanField()

    def __str__(self):
        return '{} {}'.format(self.student.user.first_name, self.student.user.last_name)