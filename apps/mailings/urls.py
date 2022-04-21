from rest_framework.routers import DefaultRouter

from apps.mailings import views

router = DefaultRouter()
router.register('', views.MailingViewSet, basename='mailings')

urlpatterns = router.urls
