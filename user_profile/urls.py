from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('storefront/', views.user_store, name='storefront'),
    path('storefront/<str:username>/', views.other_store, name='storefront_other'),
]
