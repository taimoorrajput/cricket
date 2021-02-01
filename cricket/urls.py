from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stadium/', include('stadium.urls')),
    path('team/', include('team.urls')),
    path('tournament/', include('tournament.urls')),
]
