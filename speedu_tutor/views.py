from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from . import app_settings
from .forms import LoginForm, ChangePasswordForm


def user_login(request):

    if request.user.is_authenticated:
        return redirect('tutor', permanent=True)

    user_invalid = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            rememberme = form.cleaned_data['rememberme']

            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                if not rememberme:
                    request.session.set_expiry(900)

                return redirect('tutor', permanent=True)
            else:
                user_invalid = True                

    else:
        form = LoginForm()
    
    context = {
        'form': form,
        'user_invalid': user_invalid,
    }

    return render(request, 'speedu_tutor/auth/login.html', context=context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index', permanent=True)
    return redirect('tutor', permanent=True)

@login_required
def index(request):
    context = {
        'title': 'Inicio - SpeedU Tutor',
    }
    return render(request, 'speedu_tutor/index.html', context=context)

@login_required
def profile(request):
    context = {
        'title': '{} - SpeedU Tutor'.format(request.user.student),
    }

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():

            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            if new_password == confirm_password:
                if request.user.check_password(current_password):
                    request.user.set_password(new_password)
                    request.user.save()
                    update_session_auth_hash(request, request.user)
                    context['message'] = {
                        'text': 'La contraseña se actualizó correctamente.',
                        'type': 'success',
                    }
                else:
                    context['message'] = {
                        'text': 'La contraseña es incorrecta.',
                        'type': 'error',
                    }
            else:
                context['message'] = {
                    'text': 'Las contraseñas no coinciden.',
                    'type': 'error',
                }
        else:
            context['message'] = {
                'text': 'Formulario incorrecto.',
                'type': 'error'
            }
    else:
        form = ChangePasswordForm()
    
    context['form'] = form

    return render(request, 'speedu_tutor/profile.html', context=context)

@login_required
def tutorial_detail(request, pk):
    return render(request, 'speedu_tutor/index.html')

def offline(request):
    return render(request, 'speedu_tutor/layout.html', context={'title': 'Offline - SpeedU Tutor'})


def service_worker(request):
    response = HttpResponse(open(app_settings.PWA_SERVICE_WORKER_PATH).read(), content_type='application/javascript')
    return response

def manifest(request):
    return render(request, 'speedu_tutor/pwa/manifest.json')


