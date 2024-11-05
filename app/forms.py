from django import forms

class FontTimes(forms.Form):
    word = forms.CharField()
    n = forms.IntegerField()
class HeyYou(forms.Form):
    name = forms.CharField()
class HowOld(forms.Form):
    year = forms.IntegerField()
    birth = forms.IntegerField()
class CANITAKEYOURORDER(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()
class TeenSum(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()
class XYZthere(forms.Form):
    string = forms.CharField()
class Median(forms.Form):
    array = forms.CharField()