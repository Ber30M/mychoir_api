from django.db import models

class Chant(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    Key = models.CharField(max_length=12)
    paroles = models.TextField(max_length=50)
    Partie_eucharistique = models.CharField(max_length=50)
    temps_liturgique = models.CharField(max_length=50)
    
class Choriste(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=12)
    voice = models.CharField(max_length=12)
    
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    is_present = models.BooleanField()
    event= models.ForeignKey(Choriste, on_delete=models.PROTECT)
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
class Temps_liturgique(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    date_begin = models.DateField()
    date_end = models.DateField()
class Partie_eucharistique(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    
    
    
