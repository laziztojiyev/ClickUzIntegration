from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .swagger import urlpatterns as swagger_patterns
from core import settings
from apps.clickpayment.views import set_language


urlpatterns = [
    path('i18n/set_language/', set_language, name='set_language'),
    path('rosetta/', include('rosetta.urls')),
    path("admin/", admin.site.urls),
    path("", include("apps.clickpayment.urls")),
]


urlpatterns += swagger_patterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
