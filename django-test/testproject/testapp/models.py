from django.db import models
from django.core import validators


class Person(models.Model):
    name = models.CharField(max_length=200)
    coolness = models.BooleanField(default=False)


class School(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Person', on_delete=models.PROTECT)


class Teacher(models.Model):
    person = models.ForeignKey('Person', on_delete=models.PROTECT)
    school = models.ForeignKey('School', on_delete=models.PROTECT)
    salary = models.PositiveIntegerField()


class Student(models.Model):
    person = models.ForeignKey('Person', on_delete=models.PROTECT)
    school = models.ForeignKey('School', on_delete=models.PROTECT)
    grade = models.FloatField(validators=[validators.MinValueValidator(0.0),
                                          validators.MinValueValidator(5.0)])