
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from khademi_pharmacy import settings
from .views import home_page

urlpatterns = [
    path('dashborad' , home_page),
    path('' , include('customer.urls')),
    path('' , include('account.urls')),

    path('' , include('medication.urls')),

    path('' , include('order.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
