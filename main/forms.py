from django import forms
from .models import University, uClass, Note, URL

class Create_uClass(forms.ModelForm):
    class Meta:
        model = uClass
        fields = ['uni', 'term', 'class_code', 'description', 'instructor']

class Create_Note(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['uClass', 'content']

class Create_URL(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['uClass', 'description', 'url']