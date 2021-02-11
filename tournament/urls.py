from rest_framework import routers
from .api.viewsets import TournamentViewSet,MatchViewSet

router = routers.SimpleRouter()
router.register('tournament', TournamentViewSet,basename='tournament')
router.register('match', MatchViewSet,basename='match')

urlpatterns = router.urls