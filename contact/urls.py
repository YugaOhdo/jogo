from django.urls import path
from contact import views


app_name = 'contact'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
    #contact (CRUD)  meio que um formato padrão 
    path('contact/<int:contact_id>/detail', views.oneContact, name='oneContact'),
    path('contact/create/', views.create, name='create'),  #não tem o ID pq não foi criado
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('user/register/', views.registerUser, name='registerUser'),
    path('user/update/', views.userUpdate, name='userUpdate'),
    path('user/login/', views.userLogin, name='login'),
    path('user/logout/', views.userLogout, name='logout'),



]
