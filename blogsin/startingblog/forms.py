from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body','header_image', 'upload')

#A MODELFORM helps to create fields for the model

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a Title Placeholder'}),
            'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }