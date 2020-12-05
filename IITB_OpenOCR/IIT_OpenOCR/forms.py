from django import forms
from .models import sets, users, book


class setsform(forms.ModelForm):

    class Meta:
        model = sets
        fields = "__all__"