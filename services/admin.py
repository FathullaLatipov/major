from django.contrib import admin

from .models import ServiceModel, BannerModel, ServiceImagesModel


class ServiceImagesModelAdmin(admin.TabularInline):
    model = ServiceImagesModel


@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    inlines = [ServiceImagesModelAdmin, ]


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    pass
