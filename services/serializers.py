from rest_framework.serializers import ModelSerializer

from .models import ServiceImagesModel, ServiceModel, BannerModel, ResourceModel, ResourceImagesModel


class BannerSerializer(ModelSerializer):
    class Meta:
        model = BannerModel
        fields = '__all__'


class ServiceImagesModelSerializer(ModelSerializer):
    class Meta:
        model = ServiceImagesModel
        fields = '__all__'

class ServiceModelSerializer(ModelSerializer):
    service_images = ServiceImagesModelSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceModel
        fields = '__all__'
        depth = 1

class ResourceImagesModelSerializer(ModelSerializer):
    class Meta:
        model = ResourceImagesModel
        fields = '__all__'

class ResourceModelSerializer(ModelSerializer):
    service_images = ResourceImagesModelSerializer(many=True, read_only=True)

    class Meta:
        model = ResourceModel
        fields = '__all__'
        depth = 1



