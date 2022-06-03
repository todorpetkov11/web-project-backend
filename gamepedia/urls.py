from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from gamepedia import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('threads/', include('threads.urls')),
    path('', include('core.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
