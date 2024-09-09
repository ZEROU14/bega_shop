
from django import forms

class AddToCartForm(forms.Form):
    CHOICES = [(i,str(i)) for i in range(1,30)]

    quantity = forms.TypedChoiceField(choices=CHOICES, coerce=int, label='تعداد')
    quantity = forms.TypedChoiceField(choices=CHOICES, coerce=int)

    inplace = forms.BooleanField(required=False,widget=forms.HiddenInput)
