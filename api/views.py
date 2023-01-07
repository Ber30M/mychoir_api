from .models import *
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from rest_framework import permissions


class ChantViewSet(viewsets.ModelViewSet):
    queryset= Chant.objects.all()
    serializer_class= ChantSerializer

class ChoristeViewSet(viewsets.ModelViewSet):
    queryset= Choriste.objects.all()
    serializer_class= ChoristeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset= Attendance.objects.all()
    serializer_class= AttendanceSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset= Event.objects.all()
    serializer_class= EventSerializer

class Temps_liturgiqueViewSet(viewsets.ModelViewSet):
    queryset= Temps_liturgique.objects.all()
    serializer_class= Temps_liturgiqueSerializer

class Partie_eucharistiqueViewSet(viewsets.ModelViewSet):
    queryset= Partie_eucharistique.objects.all()
    serializer_class= Partie_eucharistiqueSerializer
