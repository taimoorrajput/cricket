# Generated by Django 3.1.5 on 2021-01-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_match_tournament'),
        ('team', '0003_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='match',
            field=models.ManyToManyField(to='tournament.Match'),
        ),
    ]
