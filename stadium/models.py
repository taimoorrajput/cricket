from django.db import models
import datetime

class Stadium(models.Model):
    
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        