from django import forms


class inputForm(forms.Form):
    sequence = forms.CharField(
        
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Input sequence"
        })
    )
    