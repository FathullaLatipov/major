from django.contrib import admin

from .models import ServiceModel, BannerModel, ServiceImagesModel, ResourceModel, ResourceImagesModel


class ServiceImagesModelAdmin(admin.TabularInline):
    model = ServiceImagesModel

class ResourceImagesModelAdmin(admin.TabularInline):
    model = ResourceImagesModel


@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    inlines = [ServiceImagesModelAdmin, ]

@admin.register(ResourceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    inlines = [ResourceImagesModelAdmin, ]


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    pass
