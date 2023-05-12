import django_filters as filters

from .models import Match


class MatchFilter(filters.FilterSet):
    active = filters.BooleanFilter()

    class Meta:
        model = Match
        fields = ['symbol', 'active']
