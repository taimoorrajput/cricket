from rest_framework import serializers
from ..models import Stadium
from tournament.api.serializers import MatchSerializer, MatchDetailedSerializer

class StadiumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stadium
        fields = '__all__'

class StadiumDetailSerializer(serializers.ModelSerializer):
    matches = MatchSerializer(many=True,read_only=True)

    class Meta:
        model = Stadium
        fields = ["id","name","capacity","country","matches"]
