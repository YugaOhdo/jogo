from django.urls import path
from contact import views


app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),
    path('deck/', views.showdeck, name='showdeck'),
    path('battle/', views.batalha1, name='batalha1'),
    path('battle2/', views.batalha2, name='batalha2'),
    path('battle3/', views.batalha3, name='batalha3'),
    # path('comparar/', views.comparar, name='comparar'),
    path('resultado/', views.resultado, name='resultado'),
    path('history/', views.history, name='history'),
    path('history2/', views.history2, name='history2'),
    path('history3/', views.history3, name='history3')



]
