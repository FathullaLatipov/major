from django.contrib import admin
from django.urls import path, include

from services.views import BannerView, ServiceView, ServiceImageView
from .yasg import urlpatterns as doc_urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'banner', BannerView, basename='banner')
router.register(r'service', ServiceView, basename='service')
router.register(r'service-images', ServiceImageView, basename='service-images')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]


urlpatterns += doc_urls
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)