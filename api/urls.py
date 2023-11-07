from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.notification import NotificationModelViewSet
from api.views.notification_center import NotificationCenterModelViewSet
from api.views.plant import PlantModelViewSet
from api.views.user import UserView, ChangePasswordView

router = DefaultRouter()
router.register(r'plants', PlantModelViewSet, basename='plant')
router.register(r'notifications', NotificationModelViewSet, basename='notification')
router.register(r'notification-centers', NotificationCenterModelViewSet, basename='notification_center')


urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserView.as_view(), name='user'),
    path('user/change-password', ChangePasswordView.as_view(), name='user-change-password'),
]
