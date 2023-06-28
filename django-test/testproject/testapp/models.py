from django.db import models
from django.core import validators


class Person(models.Model):
    name = models.CharField(max_length=200)
    coolness = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class School(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Person', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    person = models.ForeignKey('Person', on_delete=models.PROTECT)
    school = models.ForeignKey('School', on_delete=models.PROTECT)
    salary = models.PositiveIntegerField()


class Student(models.Model):
    person = models.ForeignKey('Person', on_delete=models.PROTECT)
    school = models.ForeignKey('School', on_delete=models.PROTECT)
    grade = models.FloatField(validators=[validators.MinValueValidator(0.0),
                                          validators.MaxValueValidator(5.0)])
