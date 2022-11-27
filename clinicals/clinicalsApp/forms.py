from django import forms
from clinicalsApp import models

class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = "__all__"


class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = models.ClinicalData
        fields = "__all__"
