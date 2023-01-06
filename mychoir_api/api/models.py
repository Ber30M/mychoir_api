from django.db import models

class Chant(models.Model):
    id = models.AutoField()
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    paroles = models.TextField(max_length=50)
    moment_eucharistique = models.CharField(max_length=50)
    temps_liturgique = models.CharField(max_length=50)
    
class Choriste(models.Model):
    id = models.AutoField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=12)
    voice = models.CharField(max_length=12)
    
class Event(models.Model):
    id = models.AutoField()
    nom = models.CharField(max_length=50)
    lieu = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    event= models.ForeignKey(on_delete=models.PROTECT)
class Event(models.Model):
    id = models.AutoField()
    nom = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
    
    
    
