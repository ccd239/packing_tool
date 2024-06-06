from django import forms

class ProductSizesForm(forms.Form):
    length = forms.IntegerField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    weight =forms.IntegerField()