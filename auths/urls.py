from django.urls import path
from auths import views


auths_urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('refresh_token/', views.RefreshTokenAPIView.as_view(), name='login'),
]
