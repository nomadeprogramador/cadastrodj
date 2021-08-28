from django import forms
from django.forms.fields import DateField
from .models import Funcionario
from cadastrodj import settings

class FuncionarioForm(forms.ModelForm):
    data_nascimento=DateField(input_formats=settings.DATE_INPUT_FORMATS,help_text='d-m-yyyy Ex:07-08-1997')
    class Meta:
        model = Funcionario
        fields = '__all__'
