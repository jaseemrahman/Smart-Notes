
from django import forms
from .models import Note
# from django import ModelForm
from django.core.exceptions import ValidationError

class NoteForm(forms.ModelForm):
    class Meta:
        model= Note 
        fields = ('title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control my-5'}),
            'text':forms.Textarea(attrs={'class':'form-control mb-5'})
        }
        labels = {
            'text':'share your thoughts here:'
        }

    def clean_title(self):
        title= self.cleaned_data["title"]
        # if 'Django' not in title:
        #     raise ValidationError('We only accept notes about Django')
        return title
