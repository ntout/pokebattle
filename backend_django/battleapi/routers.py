from rest_framework import routers
from game.viewsets import BattleViewSet

router = routers.DefaultRouter()

router.register(r'battles', BattleViewSet)