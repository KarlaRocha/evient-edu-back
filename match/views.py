from rest_framework import generics
from django_filters import rest_framework as filters
from django.http import JsonResponse

from .models import Match
from .serializers import MatchSerializer
from use_cases.get_matches.controller import Controller as GetMatchesController


# class MatchList(generics.ListCreateAPIView):
#     queryset = Match.objects.all()
#     filter_backends = (filters.DjangoFilterBackend,)
#     serializer_class = MatchSerializer

class MatchList(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        params = self._parse_params(request.query_params)
        controller = GetMatchesController()
        response = controller.get_product(params)
        if response:
            return JsonResponse({"success": True, "data": response}, status=200)
        else:
            return JsonResponse({"success": True, "message": "Fail"}, status=400)
        
    def _parse_params(self, params):
        return {
            "active": self._get_active_param(params),
            "player": self._get_player_param(params)
        }
    
    def _get_active_param(self, params):
        active = None
        try:
            active = params['active']
        except:
            pass
        if(active == 'true'):
            active = True
        elif (active == 'false'):
            active = False
        return active
    
    def _get_player_param(self, params):
        player = None
        try:
            player = params["player"]
        except:
            pass
        return player


class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = MatchSerializer
