from rest_framework import serializers
from .models import Match
from .filters import MatchFilter


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        filter_class = MatchFilter
