from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

class ProductImagesStorage(S3Boto3Storage):
    location = settings.PRODUCT_IMAGES_LOCATION  

class ProductFilesStorage(S3Boto3Storage):
    location = settings.PRODUCT_FILES_LOCATION        