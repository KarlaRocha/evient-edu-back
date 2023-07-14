import imp
from rest_framework.views import APIView
from rest_framework import permissions

from django.http import JsonResponse

from use_cases.login.controller import Controller as Logincontroller
from use_cases.refresh_token.controller import Controller as RefreshTokenController


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        controller = Logincontroller()
        try:
            response = controller.login(request.data)
            return response
        except Exception as error:
            return JsonResponse({"success": False, "message": f"Error: {error}"}, status=400)


class RefreshTokenAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        controller = RefreshTokenController()
        try:
            response = controller.refresh_token({"refreshtoken": request.COOKIES.get("refreshtoken")})
            return response
        except Exception as error:
            return JsonResponse({"success": False, "message": f"Error: {error}"}, status=400)
