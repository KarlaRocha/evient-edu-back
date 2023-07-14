import jwt
import datetime

from rest_framework.response import Response
from rest_framework import exceptions

from django.conf import settings

from users.models import User



class Gateway:
    def refresh_token(self, refresh_token_data: dict) -> Response:
        refresh_token = refresh_token_data["refreshtoken"]
        if not refresh_token:
            raise exceptions.AuthenticationFailed("Authentication credentials were not provided.")
        try:
            payload = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("expired refresh token, please login again.")
        except Exception as error:
            raise exceptions.AuthenticationFailed(str(error))

        user = User.objects.filter(id=payload.get("user_id")).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")
        if not user.is_active:
            raise exceptions.AuthenticationFailed("user is inactive")


        access_token = self.generate_access_token(user)
        return Response({"access_token": access_token})

    def generate_access_token(self, user):
        access_token_payload = {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
            "iat": datetime.datetime.utcnow(),
        }
        access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm="HS256").decode("utf-8")
        return access_token
