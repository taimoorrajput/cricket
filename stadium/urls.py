from rest_framework import routers
from .api.viewsets import StadiumViewSet

router = routers.SimpleRouter()
router.register(r'stadium', StadiumViewSet, basename='stadium/<int:pk/>')

urlpatterns = router.urls