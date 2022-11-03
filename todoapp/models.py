
from django.db import models

class todo(models.Model):
     title=models.CharField(max_length=200)
     date = models.DateTimeField()

     def __str__(self):
         return self.date




