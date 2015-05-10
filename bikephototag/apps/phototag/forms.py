from django import forms
# import autocomplete_light

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field
# from crispy_forms.bootstrap import StrictButton


class AddPhotoForm(forms.Form):
    img = forms.FileField()
    # latitude
    # longitude

class RegistationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

# class NewEventForm(forms.Form):
