from datetime import date
from django.db import models
from datetime import date

# Create your models here.

# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

PLCIE = models.IntegerChoices('PLEC','Kobieta Męzczyzna Inna')


SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    pseudonim = models.CharField(max_length=80, default="")
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"Person : {self.name}, dodana w {self.month_added}, o rozmiarze koszuli {self.shirt_size}.\n" 

class Osoba(models.Model):
    PLEC_CHOICES=(
        ("K", "Kobieta"),
        ("M", "Męzczyzna"),
        ("I", "Inna"),
    )
    
    imie = models.CharField(max_length = 40, blank = False, null = False)
    nazwisko = models.CharField(max_length = 60, blank = False, null = False)
    plec = models.IntegerField(choices=PLCIE.choices, default=PLCIE.choices[2][0])
    stanowisko = models.ForeignKey('Stanowisko', on_delete = models.CASCADE)
    data_dodania = models.DateField(default= date.today, blank=False, null = False)
    
    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        ordering = ["nazwisko"]
class Stanowisko(models.Model):
    nazwa = models.CharField(max_length = 80, blank = False, null = False)
    opis = models.TextField(blank = False, null = False)
    
    def __str__(self):
        return self.nazwa