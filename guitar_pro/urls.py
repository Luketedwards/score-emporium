from django.urls import path
from . import views

urlpatterns = [
    path('', views.guitar_pro, name='guitar_pro'),
    
]