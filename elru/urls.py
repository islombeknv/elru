from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from clickuz import ClickUz
from payments.views import ClickView, TestView
from paycomuz import Paycom

# paycom = Paycom()
# url = paycom.create_initialization(amount=5.00, order_id='197', return_url='https://example.com/success/')
# print(url)
# url = ClickUz.generate_url(order_id='1', amount='15000000')
# print(url)


urlpatterns = i18n_patterns(
    path('click/transaction/', ClickView.as_view()),
    path('admin/', admin.site.urls),
    path('accounts/', include('rest_registration.api.urls')),
    path('', include('books.urls')),
    path('news/', include('blog.urls')),
    path('user/', include('accounts.urls')),
    path('blocks/', include('blocks.urls')),
    path('order/', include('orders.urls')),
    path('paycom/', TestView.as_view()),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
