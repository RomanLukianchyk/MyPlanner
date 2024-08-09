from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from categories import views
from users import views as user_views
from core import views as core_views
from notes import views as notes_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('', core_views.home, name='home'),
    path('tasks/', include('tasks.urls')),
    path('categories/', include('categories.urls')),
    path('documents/', include('documents.urls')),
    path('calendar/', include('kalendar.urls')),
    path('notes/', include('notes.urls')),
    path('users/', include('users.urls')),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('register/', user_views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)