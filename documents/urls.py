from django.urls import path
from documents import views


urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('upload/', views.document_upload, name='document_upload'),
    path('<int:pk>/', views.document_detail, name='document_detail'),
    path('<int:pk>/delete/', views.document_delete, name='document_delete'),
]