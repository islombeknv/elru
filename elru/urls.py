from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('auth/api/', include(api_urlpatterns)),
    path('', include('books.urls')),
    path('news/', include('blog.urls')),
    path('user/', include('accounts.urls')),
    path('blocks/', include('blocks.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
