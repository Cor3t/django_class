from django.urls import path, include
from store1 import views

urlpatterns =  [
    path('', views.home),
    path('createpost/', views.createpost, name='createpost'),
    path('login/', views.auth_login, name='login'),
    path('register', views.register, name='register')
]