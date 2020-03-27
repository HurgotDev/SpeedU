from django.contrib import admin

from .models import Institution, Career, Subject, Student, Tutor, Schedule, Tutorial, Competitor

# Register your models here.
admin.site.register(Institution)
admin.site.register(Career)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Schedule)
admin.site.register(Tutorial)
admin.site.register(Competitor)
