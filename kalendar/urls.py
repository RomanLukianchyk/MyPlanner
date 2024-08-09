from django.urls import path
from kalendar import views

urlpatterns = [
    path('', views.CalendarEventListView.as_view(), name='calendar_view'),
    path('create/', views.event_create, name='event_create'),
    path('<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('<int:pk>/', views.CalendarEventDetailView.as_view(), name='event_detail'),
]
