from rest_framework import generics
from django.http import JsonResponse

from use_cases.get_matches.controller import Controller as GetMatchesController
from use_cases.get_match.controller import Controller as GetMatchController
from use_cases.create_match.controller import Controller as CreateMatchController


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


class MatchDetail(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        id = kwargs["pk"]
        controller = GetMatchController()
        data = controller.get_match(id)
        return JsonResponse({"success": True, "data": data}, status=200)


class MatchCreate(generics.GenericAPIView):
    def put(self, request, *args, **kwargs):
        controller = CreateMatchController()
        match_id = controller.create_match(request.data)
        return JsonResponse({"success": True, "match_id": match_id}, status=200)