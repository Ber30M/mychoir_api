from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class ChantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chant
        fields = '__all__'

class ChoristeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choriste
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
class Temps_liturgiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temps_liturgique
        fields = '__all__'
class Partie_eucharistiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partie_eucharistique
        fields = '__all__'

