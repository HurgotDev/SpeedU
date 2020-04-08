from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=150)

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
    cc = models.IntegerField()
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()
    semester = models.IntegerField()
    career = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.name, self.lastname)

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
        return '{} {}'.format(self.student.name, self.student.lastname)

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

class Competitor(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attended_tutor = models.BooleanField()
    attended_student = models.BooleanField()

    def __str__(self):
        return '{} {}'.format(self.student.name, self.student.lastname)