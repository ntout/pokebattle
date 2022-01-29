from rest_framework import viewsets
from .serializers import BattleSerializer
from.models import Battle


class BattleViewSet(viewsets.ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer