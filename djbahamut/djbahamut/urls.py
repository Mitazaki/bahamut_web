"""
URL configuration for djbahamut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# filepath: /home/dl/web/djbahamut/djbahamut/urls.py
from django.contrib import admin
from django.urls import path, include
from discordlogin import views as discord_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/user/', discord_views.get_authenticated_user, name='get_authenticated_user'),
    path('oauth2/', discord_views.home, name='oauth2'),
    path('oauth2/login/', discord_views.discord_login, name='oauth2_login'),
    path('login/redirect/', discord_views.discord_login_redirect, name='discord_login_redirect'),
    path('', include('dashboard.urls')),  # Include the dashboard URLs
]