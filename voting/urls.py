from django.urls import path
from . import views

urlpatterns = [
    path('', views.requests, name='requests'),
    path('completed_requests', views.completed_requests, name='completed_requests'),
    path('make_request/', views.make_request, name='make_request'),
    path('like_post/<int:pk>', views.like_post, name='like_post'),
    path('like_post_completed/<int:pk>', views.like_post_completed, name='like_post_completed'),
    path('comment_post/<int:pk>', views.comment_post, name='comment_post'),
    path('comment_post_completed/<int:pk>', views.comment_post_completed, name='comment_post_completed'),
    path('dislike_post/<int:pk>', views.dislike_post, name='dislike_post'),
    path('dislike_post_completed/<int:pk>', views.dislike_post_completed, name='dislike_post_completed'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('submit_score/<int:pk>', views.create_submission, name='create_submission'),
    path('accept_submission/<int:pk>/<int:score_pk>', views.accept_score_submission, name='accept_score_submission'),
    
]