from django.contrib import admin
from django.urls import path, include

from services.views import BannerView, ServiceView, ServiceImageView, ResourceView, ResourceImageView
from .yasg import urlpatterns as doc_urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# ResourceView
# ResourceImageView

router = DefaultRouter()
router.register(r'banner', BannerView, basename='banner')
router.register(r'service', ServiceView, basename='service')
router.register(r'service-images', ServiceImageView, basename='service-images')
router.register(r'resource', ResourceView, basename='resource')
router.register(r'resource-images', ResourceImageView, basename='resource-images')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]


urlpatterns += doc_urls
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)