from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .model import Player

class PlayerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'
            
    class Meta:
        model = Player
        fields = 'username',
        
from django import forms

class BotaoForm(forms.Form):
    botao_id = forms.CharField()