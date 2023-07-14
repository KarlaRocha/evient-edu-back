import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from django.middleware.csrf import CsrfViewMiddleware
from django.conf import settings

from users.models import User


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason


class SafeJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_heaader = request.headers.get("Authorization")
        if not authorization_heaader:
            return None
        try:
            # header = "Token xxxxxxxxxxxxxxxxxxxxxxxx"
            access_token = authorization_heaader.split(" ")[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("access_token expired")
        except IndexError:
            raise exceptions.AuthenticationFailed("Token prefix missing")
        except Exception as error:
            raise exceptions.AuthenticationFailed(str(error))

        user = User.objects.filter(id=payload["user_id"]).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")
        if not user.is_active:
            raise exceptions.AuthenticationFailed("user is inactive")
        
        self.enforce_csrf(request)
        return (user, None)

    def enforce_csrf(self, request):
        # Enforce CSRF validation
        check = CSRFCheck(request)
        # populates request.META["CSRF_COOKIE"], which is used in process_view()
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        print(reason)
        if reason:
            # CSRF failed, bail with explicit error message
            raise exceptions.PermissionDenied("CSRF Failed: %s" % reason)
