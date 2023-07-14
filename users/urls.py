from django.urls import path
from users import views

user_urlpatterns = [
    path('me/', views.MeAPIView.as_view(), name="me"),
]
