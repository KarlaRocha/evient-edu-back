from rest_framework import serializers
from .models import Match
from cell.serializers import CellSerializer


class MatchSerializer(serializers.ModelSerializer):
    cells = CellSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = '__all__'
