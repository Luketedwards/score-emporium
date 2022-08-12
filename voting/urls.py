from django.urls import path
from . import views

urlpatterns = [
    path('', views.requests, name='requests'),
    path('make_request/', views.make_request, name='make_request'),
    
]