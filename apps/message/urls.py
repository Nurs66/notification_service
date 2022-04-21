from rest_framework.routers import DefaultRouter

from apps.message import views

router = DefaultRouter()
router.register('', views.MessageViewSet, basename='message')

urlpatterns = router.urls
