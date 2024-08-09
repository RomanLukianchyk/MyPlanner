from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save_fast_note/', views.save_fast_note, name='save_fast_note'),
]
