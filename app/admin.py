from django.contrib import admin

# Register your models here.

from .models import Auto, Majitel, Vyrobce

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('id_auto', 'spz', 'znacka', 'typ', 'generace', 'rok_vydani', 'vykon', 'barva', 'pohon', 'najeto_km', 'hodnota_auta', 'majitel_auta', 'vyrobce_auta')
    search_fields = ('spz', 'znacka', 'typ')

@admin.register(Majitel)
class MajitelAdmin(admin.ModelAdmin):
    list_display = ('id_majitel', 'rodne_cislo', 'jmeno', 'prijmeni', 'pohlavi', 'mesto', 'ulice', 'cislo_popisne', 'fotka')
    search_fields = ('jmeno', 'prijmeni')

@admin.register(Vyrobce)
class VyrobceAdmin(admin.ModelAdmin):
    list_display = ('id_vyrobce', 'nazev', 'zeme', 'mesto', 'ulice', 'cislo_popisne', 'logo')
    search_fields = ('nazev', )