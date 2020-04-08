from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('started/', views.started, name="get-started"),
    path('newsletter/', views.newsletter, name="newsletter"),
    path('started/get_cities/', views.get_cities, name='get-cities'),
]
