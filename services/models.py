from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ServiceModel(models.Model):
    title = models.CharField(max_length=300, help_text=('Сюда надо писать название вашего услуги'))
    descriptions = RichTextUploadingField(verbose_name=('service_description'),
                                          help_text=('Сюда надо писать описания для вашего услуги'))
    image = models.FileField(upload_to='service_images', help_text=('Сюда надо загрузить изображения для вашего услуги'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=('Время обновления'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=('Время создания'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class BannerModel(models.Model):
    image = models.FileField(upload_to='banner_images', help_text=('Сюда надо загрузить изображения для вашего баннера'))
    title = models.CharField(max_length=200, help_text=('Сюда надо писать название вашего баннера'))
    descriptions = RichTextUploadingField(verbose_name=('banner_description'),
                                          help_text=('Сюда надо писать описания для вашего услуги'))
    link = models.TextField()
    updated_at = models.DateTimeField(auto_now=True, verbose_name=('Время обновления'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=('Время создания'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class ServiceImagesModel(models.Model):
    product = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='service_images')
    image = models.FileField(upload_to='product_images')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Изображения банера'
        verbose_name_plural = 'Изображения баннеров'


class ResourceModel(models.Model):
    image = models.FileField(upload_to='rec_images', help_text=('Сюда надо загрузить изображения для вашего ресурса'))
    title = models.CharField(max_length=200, help_text=('Сюда надо писать название вашего ресурса'))
    descriptions = RichTextUploadingField(verbose_name=('banner_description'),
                                          help_text=('Сюда надо писать описания для вашего ресурса'))
    # link = models.TextField()
    updated_at = models.DateTimeField(auto_now=True, verbose_name=('Время обновления'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=('Время создания'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'


class ResourceImagesModel(models.Model):
    product = models.ForeignKey(ResourceModel, on_delete=models.CASCADE, related_name='resource_images')
    image = models.FileField(upload_to='resource_images')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Изображения ресурса'
        verbose_name_plural = 'Изображения ресурсов'

