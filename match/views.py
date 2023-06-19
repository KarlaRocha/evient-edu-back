from rest_framework import generics
from django.http import JsonResponse

from use_cases.get_matches.controller import Controller as GetMatchesController
from use_cases.get_match.controller import Controller as GetMatchController
from use_cases.create_match.controller import Controller as CreateMatchController
from use_cases.update_match.controller import Controller as UpdateMatchController
from use_cases.update_player_move.controller import Controller as PlayerMoveController


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
        id = kwargs["pk"]
        controller = GetMatchController()
        data = controller.get_match(id)
        return JsonResponse({"success": True, "data": data}, status=200)
    
    def patch(self, request, *args, **kwargs):
        id = kwargs["pk"]
        payload = request.data
        print(id)
        print(payload)
        controller = UpdateMatchController()
        success = controller.update_product(id, payload)
        return JsonResponse({"success": success}, status=200)


class MatchCreate(generics.GenericAPIView):
    def put(self, request, *args, **kwargs):
        controller = CreateMatchController()
        match_id = controller.create_match(request.data)
        return JsonResponse({"success": True, "match_id": match_id}, status=200)


class PlayerMove(generics.GenericAPIView):
    def patch(self, request, *args, **kwargs):
        controller = PlayerMoveController()
        match_id = kwargs["pk"]
        player_id = request.data["player_id"]
        cell_id = request.data["cell_id"]
        response = controller.update_player_move(match_id, player_id, cell_id)
        return JsonResponse(response, status=200)
