from django.contrib import admin

from .models import Person, School, Teacher, Student

admin.site.register(Person)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
