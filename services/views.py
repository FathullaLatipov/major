from django.shortcuts import render
from .models import BannerModel, ServiceModel, ServiceImagesModel, ResourceModel, ResourceImagesModel
from .serializers import BannerSerializer, ServiceModelSerializer, ServiceImagesModelSerializer, ResourceImagesModelSerializer, ResourceModelSerializer
from rest_framework.viewsets import GenericViewSet, mixins


class BannerView(mixins.RetrieveModelMixin, mixins.ListModelMixin,GenericViewSet):
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializer


class ServiceView(mixins.RetrieveModelMixin, mixins.ListModelMixin,GenericViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceModelSerializer


class ServiceImageView(mixins.RetrieveModelMixin, mixins.ListModelMixin,GenericViewSet):
    queryset = ServiceImagesModel.objects.all()
    serializer_class = ServiceImagesModelSerializer


class ResourceView(mixins.RetrieveModelMixin, mixins.ListModelMixin,GenericViewSet):
    queryset = ResourceModel.objects.all()
    serializer_class = ResourceModelSerializer


class ResourceImageView(mixins.RetrieveModelMixin, mixins.ListModelMixin,GenericViewSet):
    queryset = ResourceImagesModel.objects.all()
    serializer_class = ResourceImagesModelSerializer