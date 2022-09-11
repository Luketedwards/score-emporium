from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('storefront/<str:storevendor>/', views.user_store, name='storefront'),
    path('storefront/<str:username>/', views.other_store, name='storefront_other'),
    path('purchased-scores/', views.purchased_scores, name='purchased_scores'),
    path('vendor-signup/', views.vendor_signup, name='vendor_signup'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

]
