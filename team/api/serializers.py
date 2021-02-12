from rest_framework import serializers
from ..models import Team,Player
from tournament.api.serializers import MatchDetailedSerializer, MatchSerializer

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

class TeamDetailSerializer(serializers.ModelSerializer):
    matches = MatchSerializer(many=True,read_only=True)

    class Meta:
        model = Team
        fields = ['id','country','matches']

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'

class PlayerDetailSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True,read_only=True)

    class Meta:
        model = Player
        fields = ['id','name','age','category','teams']
        