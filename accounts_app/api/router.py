from rest_framework import routers

from accounts_app.api.views.account import UserCreateView

api_router = routers.DefaultRouter()

api_router.register('registration', UserCreateView)
