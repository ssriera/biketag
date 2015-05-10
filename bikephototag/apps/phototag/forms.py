from django import forms
# import autocomplete_light

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field
# from crispy_forms.bootstrap import StrictButton


class AddPhotoForm(forms.Form):
    img = forms.FileField()
    # latitude
    # longitude
