from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('task/', include('task.urls')),
    path('', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]