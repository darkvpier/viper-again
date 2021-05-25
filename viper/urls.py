
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('', include('apps.core.urls')),
    path('events/', include('apps.event.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
