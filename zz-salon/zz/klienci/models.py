from django.db import models


# Create your models here.

class Sex(models.Model):
    sex = models.CharField('Płeć', max_length=10)
    def __str__(self):
        return self.sex
    class Meta:
        verbose_name = 'Płeć'
        verbose_name_plural = 'Płcie'
        

class AnimalType(models.Model):
    gatunek = models.CharField('Gatunek', max_length=20)
    def __str__(self):
        return self.gatunek
    class Meta:
        verbose_name = 'Gatunek'
        verbose_name_plural = 'Gatunki'

class Zwierze(models.Model):
    imie = models.CharField(max_length=30)
    create_date = models.DateTimeField('Data dodania', auto_now=True)
    last_visit = models.DateField('Ostatnia wizyta', null=True, blank=True)
    next_visit = models.DateField('Następna wizyta', null=True, blank=True)
    phone_number = models.CharField('Numer tel.', max_length=9, null=True)
    email = models.EmailField('adres email', blank=True)
    owner = models.CharField('Właściciel', max_length=20, null=True)
    city = models.CharField('Miejscowość', max_length=20, default="Brzoza", blank=True)
    year_birth = models.IntegerField('Data urodzenia', default='2020', null=True, blank=True)
    sex = models.ForeignKey(Sex, on_delete=models.RESTRICT, null=True)
    gatunek = models.ForeignKey(AnimalType, on_delete=models.RESTRICT, null=True, )
    breed = models.CharField('Rasa', max_length=30, null=True, blank=True)
    comments = models.TextField('Uwagi', blank=True)
    
    def fullname(self):
        return f"{self.imie} {self.owner}"
    def __str__(self):
        return self.fullname()
    class Meta:
        verbose_name = 'Zwierze'
        verbose_name_plural = 'Zwierzaki'


class Wizyty(models.Model):
    zwierze = models.ForeignKey(Zwierze, on_delete=models.CASCADE)
    visit_date = models.DateField('Data wizyty')
    visit_time = models.TimeField('Godzina wizyty', null=True)
    create_date = models.DateTimeField('Data dodania', auto_now=True)

    def fullname(self):
        return f"{self.zwierze} {self.visit_date}"
    def __str__(self):
        return self.fullname()
    class Meta:
        verbose_name = 'Wizyta'
        verbose_name_plural = 'Wizyty'