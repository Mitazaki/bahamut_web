# filepath: /home/dl/web/djbahamut/dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'dashboard/login.html')

@login_required(login_url='/oauth2/login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')