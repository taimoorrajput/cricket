from django.db import models
import datetime
from tournament.models import Match

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    country = models.CharField(max_length=100)
    match = models.ForeignKey(Match, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name