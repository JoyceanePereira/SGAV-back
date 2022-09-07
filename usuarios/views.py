from audioop import reverse
from contextlib import redirect_stderr
from pyexpat.errors import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Perfil
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime

# Create your views here.

def home (request):
    return render (request, 'index.html')

def perfil (request):
    return render (request, 'perfil.html')

def dashboard (request):
    return render (request, 'dashboard.html')

def card (request):
    return render (request, 'card.html')

def cardpessoal (request):
    return render (request, 'card-pessoal.html')

def login(request):
    '''Realiza login no sistema'''
    if request.user and request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    template_name = 'index.html'
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        remember_me = request.POST.get('remember_me')
        
        if email == "":
            messages.error(request, 'O campo "e-mail" não pode ficar vazio')
            return redirect('login')
        
        if senha == "":
            messages.error(request, 'O campo "senha" não pode ficar vazio')
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:                
                auth.login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuário ou senha incorretos')
                return redirect('login')
        else:
            messages.error(request, 'Este usuário não existe')
            return redirect('login')
    return render(request, template_name)



