from django import forms
from .models import *


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        exclude = [""]

