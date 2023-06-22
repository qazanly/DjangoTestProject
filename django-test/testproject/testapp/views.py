from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer


class PersonAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
