from django import forms

class PredictionForm(forms.Form):
    house_size = forms.FloatField(
        label='House Size (sq ft)',
        min_value=20,
        max_value=10000,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )