from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # <-- ici on nomme la route 'home'
    path('proprietes/', views.proprietes, name='proprietes'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('propriete/<int:id>/', views.detail_propriete, name='detail'),
]