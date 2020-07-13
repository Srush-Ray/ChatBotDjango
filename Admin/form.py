from django import forms
from .models import Query_table

class Forminfo(forms.ModelForm):    
    class Meta:
        model = Query_table
        fields = '__all__'