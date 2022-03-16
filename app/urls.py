from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.authtoken.views import obtain_auth_token
from accounts_app.api.router import api_router as account_router
from media_app.api.router import api_router as media_router


urlpatterns = [
    path('api/v1/token-auth/', obtain_auth_token, name='api-token-auth'),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/v1/', include(account_router.urls)),
    path('api/v1/', include(media_router.urls)),
]

