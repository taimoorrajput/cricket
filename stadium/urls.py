from rest_framework import routers
from .api.viewsets import StadiumViewSet

router = routers.SimpleRouter()
router.register('stadium', StadiumViewSet, basename='stadium')

urlpatterns = router.urls