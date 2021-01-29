from rest_framework import routers
from .api.viewsets import TeamViewSet,PlayerViewSet

router = routers.SimpleRouter()
router.register(r'team', TeamViewSet,basename='team/<int:pk>')
router.register(r'player', PlayerViewSet,basename='player/<int:pk>')

urlpatterns = router.urls