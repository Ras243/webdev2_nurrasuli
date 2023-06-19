from django.urls import path
# from .views import *
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    # path('post/', views.post, name='post'), 
    path('post/<str:pk>/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),

    # CRUD PATHS
    path('create_post/', views.createPost, name='create_post'),
    path('update_post/<str:pk>/', views.updatePost, name='update_post'),
    path('delete_post/<str:pk>/', views.deletePost, name='delete_post'),
]


