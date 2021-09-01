from django.contrib import admin

# Register your models here.
from .models import Voyage,Excursion,Destination

class excursion(admin.ModelAdmin):
    list_display = ('nom','option',)

class voyage(admin.ModelAdmin):
    list_display = ('nom','duree','photo','prix','description','Excursion',)

class destination(admin.ModelAdmin):
    list_display = ('pays','Voyage',)


admin.site.register(Voyage,voyage)
admin.site.register(Destination,destination)
admin.site.register(Excursion,excursion)