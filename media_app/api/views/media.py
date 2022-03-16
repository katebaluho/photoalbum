from django.http import FileResponse
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from notification_app.utils import get_email_top_photo
from ..serializer.media import MediaSerializer, MediaCreateSerializer, MediaUpdateSerializer
from ...models import Media
from ...utils import create_animation


class MediaView(GenericViewSet, ListModelMixin, RetrieveModelMixin,
                UpdateModelMixin,
                CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Media.objects.all()
    actions_serializers = {'list': MediaSerializer,
                           'retrieve': MediaSerializer,
                           'create': MediaCreateSerializer,
                           'update': MediaUpdateSerializer,
                           'partial_update': MediaUpdateSerializer,
                           }
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)

    def get_queryset(self):
        user = self.request.user
        return user.photos.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_counter_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get', ], detail=False, serializer_class=MediaSerializer)
    def top_ten_download(self, *args, **kwargs):
        print(get_email_top_photo())
        photos = Media.objects.order_by('-counter_views')[:10]
        path = create_animation((p.file.url.split('/')[-1] for p in photos))
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='top_ten.webm')
