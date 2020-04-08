from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def index(request):
    return render(request, 'speedu_tutor/index.html')


