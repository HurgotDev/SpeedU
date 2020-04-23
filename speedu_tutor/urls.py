from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    url('^serviceworker.js$', views.service_worker),
    url('^manifest.json$', views.manifest),

    path('tutor/', views.index, name='tutor'),
    path('offline/', views.offline),
    path('tutor/profile/', views.profile, name='profile'),

    path('tutor/tutorial/<int:pk>/', views.tutorial_detail, name='tutorial-detail'),   
]
