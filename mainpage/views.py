from django.shortcuts import render
from django.urls import reverse

MENU_LINKS_ONE_PAGE = {
    'home': '#home',
    'about': '#about',
    'contact': '#contact',
}
MENU_LINKS_PAGE_OUT = {
    'home': '/#home',
    'about': '/#about',
    'contact': '/#contact',
}

def index(request):
    context = {
        'page_title': 'Inicio',
        'menu_links': MENU_LINKS_ONE_PAGE,
    }
    return render(request, 'mainpage/index.html', context=context)

def started(request):
    context = {
        'page_title': "Empezar",
        'menu_links': MENU_LINKS_PAGE_OUT,
    }
    return render(request, 'mainpage/started.html', context=context)
