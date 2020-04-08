from django.urls import path, include

from . import views

urlpatterns = [
    path('tutor/', views.index, name='index'),    
]
