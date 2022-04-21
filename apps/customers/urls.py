from rest_framework.routers import DefaultRouter

from apps.customers import views

router = DefaultRouter()
router.register('customers', views.CustomerViewSet, basename='customers')

urlpatterns = router.urls
