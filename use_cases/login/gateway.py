import jwt
import datetime

from rest_framework.response import Response
from rest_framework import exceptions

from django.conf import settings

from users.models import User
from users.serializers import UserSerializer



class Gateway:
    def login(self, login_data: dict) -> Response:
        user = User.objects.filter(username=login_data["username"]).first()
        if not user:
            raise exceptions.AuthenticationFailed("user not found")
        if not user.check_password(login_data["password"]):
            raise exceptions.AuthenticationFailed("wrong password")
        serialized_user = UserSerializer(user, many=False).data

        access_token = self.generate_access_token(user)
        refresh_token = self.generate_refresh_token(user)

        response = Response()
        response.set_cookie(key="refreshtoken", value=refresh_token, httponly=True)
        response.data = {
            "access_token": access_token,
            "user": serialized_user,
        }
        return response

    def generate_access_token(self, user):
        access_token_payload = {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
            "iat": datetime.datetime.utcnow(),
        }
        access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm="HS256").decode("utf-8")
        return access_token

    def generate_refresh_token(self, user):
        refresh_token_payload = {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
            "iat": datetime.datetime.utcnow()
        }
        refresh_token = jwt.encode(refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm="HS256").decode("utf-8")
        return refresh_token
