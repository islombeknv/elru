from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from payments.views import TestView, ClickView

urlpatterns = [
    path('paycom/', TestView.as_view()),
    path('click/transaction/', ClickView.as_view())
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
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

from clickuz import ClickUz
url = ClickUz.generate_url(order_id='1', amount='100', return_url='https://elru.cf')
print(url)

from paycomuz import Paycom
paycom = Paycom()
url = paycom.create_initialization(amount=5.00, order_id='197', return_url='https://example.com/success/')
print(url)
