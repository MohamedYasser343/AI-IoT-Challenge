from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cropdata/', include('handle_esp.urls')),
    path('users/', include('users.urls')),
]
