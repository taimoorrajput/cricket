from django.db import models
import datetime
from tournament.models import Match

class Team(models.Model):
    country = models.CharField(max_length=50)
    matches = models.ManyToManyField(Match,related_name="teams")

    def __str__(self):
        return self.country

class Player(models.Model):
    CHOICES = (
        (1, 'Bowler'),
        (2, 'Batsman'),
        (3, 'keeper'),
        (4, 'All Rounder'),
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    category = models.CharField(max_length=20,default=1,choices=CHOICES)
    teams = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="players")

    def __str__(self):
        return self.name
