from django.db import models
from django.utils.safestring import mark_safe

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