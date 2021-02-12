from rest_framework import serializers
from ..models import Tournament,Match

class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'

class TournamentDetailSerializer(serializers.ModelSerializer):

    matches = MatchSerializer(many=True, read_only=True)

    class Meta:
        model = Tournament
        fields = ['id','name','location','start_date','end_date','matches']

class MatchDetailedSerializer(serializers.ModelSerializer):

    tournament = TournamentSerializer()

    class Meta:
        model = Match
        fields = ['id','toss','result','match_date','tournament','stadium']
        