from django.db import models
import datetime
from stadium.models import Stadium

class Tournament(models.Model):

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Match(models.Model):

    toss = models.CharField(max_length=100)
    result = models.CharField(max_length=50)
    match_date = models.DateField()
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE, related_name="matches")
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name="matches")

    def __str__(self):
        return self.toss
