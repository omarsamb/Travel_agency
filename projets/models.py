from django.db import models

# Create your models here.

class Excursion(models.Model):
    nom = models.CharField(max_length=500)
    option = models.BooleanField()

    def __str__(self):
        n = self.nom
        return n

class Voyage(models.Model):
    nom = models.CharField(max_length=500)
    duree = models.TimeField()
    photo = models.URLField()
    prix = models.IntegerField()
    description = models.TextField()
    excursion = models.ManyToManyField(Excursion,related_name='excursion',blank=True)

    def Excursion(self):
        return ",".join([str(p) for p in self.excursion.all()])

    def __str__(self):
        return self.nom

class Destination(models.Model):
    pays = models.CharField(max_length=500)
    voyage = models.ManyToManyField(Voyage,related_name='voyage',blank=True)
    def __str__(self):
        return self.pays
    def Voyage(self):
        return ",".join([str(p) for p in self.voyage.all()])



