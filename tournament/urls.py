from rest_framework import routers
from .api.viewsets import TournamentViewSet,MatchViewSet

router = routers.SimpleRouter()
router.register(r'tournament', TournamentViewSet,basename='tournament/<int:pk>')
router.register(r'match', MatchViewSet,basename='match/<int:pk>')

urlpatterns = router.urls