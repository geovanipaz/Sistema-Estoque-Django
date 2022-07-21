
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estoque_gerencia.urls')),
    path('accounts/', include('registration.backends.default.urls')),
]
