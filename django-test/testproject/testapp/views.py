from django.shortcuts import render
from rest_framework import generics

from .models import Person, School
from .serializers import PersonSerializer, SchoolSerializer


class PersonAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SchoolAPIView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
