from blog.models import Comment
from django import forms
from django.core.exceptions import ValidationError
from profanity.validators import validate_is_profane

import re

def validate_comment_text(text):
    with open("blog/badwords.txt") as f:
        CENSORED_WORDS = f.readlines()
    words = set(re.sub("[^\w]", " ",  text).split())
    if any(censored_word in words for censored_word in CENSORED_WORDS):
        raise ValidationError(f"{censored_word} is censored!")


class CommentForm(forms.ModelForm):
    name =forms.CharField(max_length=20)
    body =forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write a comment...'}),validators=[validate_comment_text])
 
    def __str__(self):
        return f"{self.body} by {self.name}"
    
    class Meta:
        model = Comment
        fields = ['name','body']

