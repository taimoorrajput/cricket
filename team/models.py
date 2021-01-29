from django.db import models
import datetime
from tournament.models import Match

class Team(models.Model):
    country = models.CharField(max_length=50)
    total_matches = models.IntegerField()
    match = models.ManyToManyField(Match)
    def __str__(self):
        return self.country

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    play_type = models.CharField(max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name
