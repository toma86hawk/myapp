from django.db import models


class Article(models.Model):
    #define content culmn 
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.content 
