from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boisson/<titre_boisson>/', views.afficherBoisson,name='afficherBoisson'),
]
