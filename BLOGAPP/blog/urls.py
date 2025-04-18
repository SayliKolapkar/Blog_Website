from django.contrib import admin
from django.urls import path, include
from . import views 
'''
from .views import *
from .views import PostListView
'''
urlpatterns = [
    path('', views.home , name='home'),
]

'''
urlpatterns = [
    path('',PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostDetailView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('register/',register, name='register'),
]
'''