from rest_framework.views import APIView
from rest_framework import generics
from django.http import JsonResponse
from .serializers import UserSerializer


class MeAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        serialized_user = UserSerializer(request.user, many=False).data
        return JsonResponse({"success": True, "data": serialized_user}, status=200)
