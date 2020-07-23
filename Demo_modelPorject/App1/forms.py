from django import forms
from django.forms import ModelForm
from App1.models import studentReg_model
class studentReg_form(ModelForm):
    class Meta:
        model=studentReg_model
        fields="__all__"
