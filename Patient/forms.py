from django import forms
from .models import Chest_Pain



class ChestPainForm(forms.ModelForm):
    class Meta:
        model = Chest_Pain
        fields = ('age','race','sex','quality','intensity','duration','associated_symptoms','similar_to_prior',
        'worsens_with','improves_with','past_medical_history_of','medication','family_and_social_hx',
        'pulse','systolic_blood_pressure','diastolic_blood_pressure','pulse_oximetry','temperature','physical_exam')
