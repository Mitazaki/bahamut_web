from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import requests
import os
from dotenv import load_dotenv
load_dotenv()


# Create your views here.
def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'message': 'Hello, World!'})

@login_required(login_url='/oauth2/login')
def get_authenticated_user(request: HttpRequest):
    user = request.user
    return JsonResponse({
        "id": user.discord_id,
        "username": user.username,
        "avatar": user.avatar,
        "email": user.email,
        "mfa_enabled": user.mfa_enabled,
        "locale": user.locale,
        "flags": user.flags,
        "public_flags": user.public_flags,
        "last_login": user.last_login
    })

def discord_login(request: HttpRequest):
    return redirect(os.getenv('DISCORD_LOGIN_URL'))

def discord_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    print(code)
    user = exchange_code(code)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    print(f'discord userset {discord_user}')
    login(request, discord_user)
    return redirect('/auth/user')

def exchange_code(code: str) -> dict:
    data = {
        'client_id': os.getenv('DISCORD_CLIENT_ID'),
        'client_secret': os.getenv('DISCORD_CLIENT_SECRET'),
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': os.getenv('DISCORD_REDIRECT_URI'),
        'scope': 'identify'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
    print(response)
    credentials = response.json()
    print(credentials)
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/users/@me', headers={'Authorization': f'Bearer {access_token}'})
    print(response)
    user = response.json()
    print(user)
    return user
