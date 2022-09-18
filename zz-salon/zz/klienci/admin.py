from django.contrib import admin
from .models import Zwierze, AnimalType, Sex, Wizyty
# Register your models here.

class ZwierzeAdmin(admin.ModelAdmin):
    list_filter = ('create_date', 'sex', 'next_visit')
    list_display = ('imie', 'owner', 'next_visit', )

admin.site.register(Wizyty)
admin.site.register(Zwierze, ZwierzeAdmin)
admin.site.register(AnimalType)
admin.site.register(Sex)