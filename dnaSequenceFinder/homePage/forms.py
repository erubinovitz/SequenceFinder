from django import forms


class inputForm(forms.Form):
    sequence = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Input sequence"
        })
    )
    