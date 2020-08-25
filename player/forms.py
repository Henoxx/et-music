from django import forms

from .utils import id_name_tuple

class ArtistForm(forms.Form):
    CHOICE = id_name_tuple()
    artist_name =  forms.ChoiceField(choices=CHOICE, initial=0)