from django.contrib import admin
from django.urls import path, include
from  django.conf.urls.static import  static
from  django.conf import settings

admin.site.site_header = "STOCK"


urlpatterns = [
    path('admin/', admin.site.urls, name='admin', kwargs={'extra_context': {'title': 'Nouveau titre'}}),
    path('', include('stock.urls')),
    path('', include('athentication.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
