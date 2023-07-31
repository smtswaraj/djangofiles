from django import forms


class uploadform(forms.Form):
    # pass
    # file_Upload = forms.FileField(),
    file_Upload = forms.ImageField()