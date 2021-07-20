from django.db import models
from django.utils.safestring import mark_safe
from datetime import datetime
from django.core.exceptions import ValidationError
import re

def validate_comment_text(text):
    with open("blog/badwords.txt") as f:
        CENSORED_WORDS = f.readlines()
    words = set(re.sub("[^\w]", " ",  text).split())
    if any(censored_word in words for censored_word in CENSORED_WORDS):
        raise ValidationError(f"{censored_word} is censored!")



class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def summary(self):
        
        overLimit = len(self.body) > 200
        if(overLimit):
            return self.body[:200] + '...'
        else:
            return self.body

    def long_summary(self):
        overLimit = len(self.body) > 1000
        if(overLimit):
            return self.body[:1000] + '...'
        else:
            return self.body        
    def date(self):
        return self.pub_date.strftime('%b %e, %Y')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField( validators=[validate_comment_text])
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"Comment by Name: {self.name}"