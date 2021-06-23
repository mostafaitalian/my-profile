from django.forms import ModelForm
from .models import MySite


class MySiteForm(ModelForm):
    

    class Meta:
        model = MySite
        fields = '__all__'