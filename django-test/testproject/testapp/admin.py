from django.contrib import admin

from .models import Person, School, Teacher, Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'school', 'grade')
    list_display_links = ('id', 'person')


admin.site.register(Person)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student, StudentAdmin)
