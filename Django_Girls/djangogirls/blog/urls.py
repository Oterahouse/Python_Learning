from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list, name = 'post_list'),
  path('post/<int:pk>/', viwes.post_detail, name = 'post_detail'),
]