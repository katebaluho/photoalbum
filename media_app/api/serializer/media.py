from django.core import validators
from rest_framework import serializers

from app import settings
from ...models import Media
from ...utils import get_url_thumbnail_image, get_url_format_image
from ...validators import MaxSizeValidator


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

    file = serializers.FileField(required=True, allow_null=False)

    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, instance):
        request = self.context["request"]
        if instance.file:
            return request.build_absolute_uri(get_url_thumbnail_image(instance.file))


class MediaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        read_only_fields = ('id', 'create_date', 'counter_views', )

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    file = serializers.FileField(required=True,
                                 allow_null=False,
                                 validators=[validators.FileExtensionValidator(settings.ALLOWED_UPLOAD_FILES,
                                                                               message='File of this format cannot be '
                                                                                       'load'),
                                             MaxSizeValidator(settings.ALLOWED_UPLOAD_FILES_SIZE_MB)])

    file_format_webp = serializers.SerializerMethodField()

    def get_file_format_webp(self, instance):
        request = self.context["request"]
        if instance.file:
            return request.build_absolute_uri(get_url_format_image(instance.file, 'WEBP'))


class MediaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('title',)



