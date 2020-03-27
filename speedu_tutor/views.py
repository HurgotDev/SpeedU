from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

@login_required
def index(request):
    return render(request, 'speedu_tutor/index.html')

def login_view(request):
    user_valid = True
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index', permanent=True)
            else:
                user_valid = False
    else:
        form = LoginForm()
    
    context = {'form': form, 'user_valid': user_valid}

    return render(request, 'speedu_tutor/login.html', context=context)
