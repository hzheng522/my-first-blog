from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'date', 'time', 'location', 'timeZone')