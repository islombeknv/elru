from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(api_urlpatterns)),

    path('', include('books.urls')),
    path('news/', include('blog.urls')),
    path('user/', include('accounts.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)