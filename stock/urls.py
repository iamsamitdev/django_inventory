from django import views
from django.urls import path
from . import views

urlpatterns = [

   # Frontend
   path('', views.index, name='index'),
   path('about', views.about, name='about'),

   # Auth
   path('register', views.register, name='register'),
   path('login', views.login_request, name='login'),

   # Backend
   path('backend/dashboard', views.dashboard, name='dashboard'),
   path('backend/logout', views.logout_request, name='logout'),
   path('backend/products', views.products, name='products'),

]
