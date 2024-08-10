from django import forms
from .models import StaffMaster


class StaffMasterForm(forms.ModelForm):
    class Meta:
        model = StaffMaster
        fields = ['name']
    