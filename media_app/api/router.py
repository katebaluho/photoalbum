from rest_framework import routers

from media_app.api.views.media import MediaView

api_router = routers.DefaultRouter()

api_router.register('photos', MediaView)

