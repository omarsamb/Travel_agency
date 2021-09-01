from django.forms import ModelForm
from .models import Voyage,Destination

class VoyageForm (ModelForm):
    class Meta:
        model = Voyage
        fields = ['nom','duree','photo','prix','description','excursion']