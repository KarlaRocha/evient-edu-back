"""TicTacToe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from player.urls import player_urlpatterns
from match.urls import match_urlpatterns
from cell.urls import cell_urlpatterns

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger/', schema_view),
]
urlpatterns += player_urlpatterns
urlpatterns += match_urlpatterns
urlpatterns += cell_urlpatterns
