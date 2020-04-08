from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import RegisterForm, NewsletterForm
from .models import Departament, City, Newsletter, Register

def index(request):
    context = {
        'page_title': 'Inicio',
        'menu_links': {
            'home': '#home',
            'about': '#about',
            'contact': '#contact',
        },
        'scroll': True,
        'message': [str(message) for message in messages.get_messages(request)]
    }
    return render(request, 'mainpage/index.html', context=context)

def get_cities(request):
    context = {}
    if request.is_ajax() and request.method == 'GET':
        departament = Departament.objects.get(pk=request.GET['departament'])
        cities = City.objects.filter(departament=departament)
        context['cities'] = cities 
    return render(request, 'mainpage/departament/cities.html', context=context)

def started(request):    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']            
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            departament = form.cleaned_data['departament']
            city = form.cleaned_data['city']
            institution = form.cleaned_data['institution']            

            try:
                register = Register.objects.get(email=email)
                messages.add_message(request, messages.SUCCESS, 'Ya se ha registrado')
                messages.add_message(request, messages.SUCCESS, 
                    'Usted ya ha solicitado nuestros servicios. Por favor espere a que unos de nuestros asesores se comunique...')
            except:
                register = Register(name=name, lastname=lastname, email=email, phone=phone,
                    city=City.objects.get(pk=city), institution=institution)
                register.save()

                messages.add_message(request, messages.SUCCESS, "¡Registro exitoso!")
                messages.add_message(request, messages.SUCCESS,
                    "Gracias por elegirnos, muy pronto uno de nuestros agentes se colocará en contacto para terminar el proceso...")
            return redirect('index', permanent=True)
    else:
        form = RegisterForm()

    context = {
        'page_title': "Empezar",
        'menu_links': {
            'home': '/#home',
            'about': '/#about',
            'contact': '/#contact'
        },
        'form': form,
    }
    return render(request, 'mainpage/started.html', context=context)

def newsletter(request):       
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():       
            email = request.POST['email']
            try:
                 _last= Newsletter.objects.get(email=email)
            except Newsletter.DoesNotExist:
                _newsletter = Newsletter(email=email)
                _newsletter.save()
            
            messages.add_message(request, messages.SUCCESS, "¡Usted se ha suscrito exitosamente al boletín informativo!")
            messages.add_message(request, messages.SUCCESS, "Le mantendremos informado de todas nuestras novedades al correo "+email)
    
    return redirect('index', permanent=True)
