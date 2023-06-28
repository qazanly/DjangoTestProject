from rest_framework import serializers

from .models import Person, School


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'coolness')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('pk', 'title', 'director')