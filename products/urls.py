from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('add_store/', views.add_product_store, name='add_product_store'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit_store/<int:product_id>/', views.edit_product_store, name='edit_product_store'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_store/<int:product_id>/', views.delete_product_store, name='delete_product_store'),
]