from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('task/', include('task.urls')),
    path('', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
