from django.urls import path
from categories import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('create/', views.category_create, name='category_create'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
]