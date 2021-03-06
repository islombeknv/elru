from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from payments.views import TestView, ClickView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paycom/', TestView.as_view()),
    path('click/transaction/', ClickView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
]

urlpatterns += i18n_patterns(
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('rest_registration.api.urls')),
    path('', include('books.urls')),
    path('news/', include('blog.urls')),
    path('user/', include('accounts.urls')),
    path('blocks/', include('blocks.urls')),
    path('order/', include('orders.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
