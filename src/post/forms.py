from django.forms import ModelForm

from .models import Post

class PostForm (ModelForm):
    class Meta:  #info sobre q hereda esta clase
        model = Post
        fields = [
            'title',
            'content'
        ]

