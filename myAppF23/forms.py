from django import forms
from myAppF23.models import Order


class Interest(forms.Form):
    Choices = [(1, 'yes'), (2, 'no')]

    interested = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect, initial=0)
    levels = forms.IntegerField(min_value=1, initial=1)
    comments = forms.CharField(widget=forms.Textarea(attrs={'label': 'Additional Comments'}), required=False)

