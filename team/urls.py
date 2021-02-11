from rest_framework import routers
from .api.viewsets import TeamViewSet,PlayerViewSet

router = routers.SimpleRouter()
router.register('team', TeamViewSet, basename='team')
router.register('player', PlayerViewSet,basename='player')

urlpatterns = router.urls