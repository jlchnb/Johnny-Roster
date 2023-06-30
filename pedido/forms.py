from django import forms
from .models import TipoComida

from django.forms import ModelForm

class TipoComidaForm(ModelForm):
    class Meta:
        model = TipoComida
        fields = "__all__"