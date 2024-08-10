from django import forms
from .models import StaffMaster,AttendanceLog


class StaffMasterForm(forms.ModelForm):
    class Meta:
        model = StaffMaster
        fields = ['name']


class AttendanceLogForm(forms.ModelForm):
    class Meta:
        model = AttendanceLog
        fields = ['staff', 'date', 'time', 'status']

    staff = forms.ModelChoiceField(queryset=StaffMaster.objects.all(), empty_label="Select Staff Member")
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    status = forms.ChoiceField(choices=[('Present', 'Present'), ('Absent', 'Absent')], widget=forms.RadioSelect)
    