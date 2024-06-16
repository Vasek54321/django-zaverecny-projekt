from django.db import models

# Create your models here.

class Auto(models.Model):
    id_auto = models.AutoField(primary_key=True)
    spz = models.CharField(max_length=10, unique=True)
    znacka = models.CharField(max_length=50)
    typ = models.CharField(max_length=50)
    generace = models.CharField(max_length=20)
    rok_vydani = models.IntegerField()
    vykon = models.IntegerField(help_text="Výkon v kW")
    barva = models.CharField(max_length=30)
    pohon = models.CharField(max_length=30)
    najeto_km = models.IntegerField()
    hodnota_auta = models.DecimalField(max_digits=10, decimal_places=2)
    fotka = models.ImageField(upload_to='fotky_aut', blank=True, null=True)
    majitel_auta = models.ForeignKey('Majitel', on_delete=models.SET_NULL, blank=True, null=True)
    vyrobce_auta = models.ForeignKey('Vyrobce', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.znacka} {self.typ} ({self.spz})"


class Majitel(models.Model):
    id_majitel = models.AutoField(primary_key=True)
    rodne_cislo = models.CharField(max_length=10, unique=True)
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    pohlavi = models.CharField(max_length=1, choices=[('M', 'Muž'), ('Z', 'Žena')])
    mesto = models.CharField(max_length=100)
    ulice = models.CharField(max_length=100)
    cislo_popisne = models.CharField(max_length=10)
    fotka = models.ImageField(upload_to='majitele/', blank=True, null=True)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Vyrobce(models.Model):
    id_vyrobce = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=100)
    zeme = models.CharField(max_length=100, null=True)
    mesto = models.CharField(max_length=100)
    ulice = models.CharField(max_length=100)
    cislo_popisne = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='vyrobci/', null=True, blank=True)

    def __str__(self):
        return self.nazev