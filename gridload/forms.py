from django import forms
from gridload import models
from .models import GridLoad, PDBShed,REBShed

class GirdLoadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, fields in self.fields.items():
            fields.label = ''
    class Meta:
        model=models.GridLoad
        fields = '__all__'


class PDBShedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, fields in self.fields.items():
            fields.label = ''
    class Meta:
        model=models.PDBShed
        fields = '__all__'


class REBShedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, fields in self.fields.items():
            fields.label = ''
    class Meta:
        model=models.REBShed
        fields = '__all__'
        
