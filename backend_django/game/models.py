from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Battle(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon_1 = models.CharField(max_length=50)
    pokemon_2 = models.CharField(max_length=50)
    move_log = ArrayField(
        models.CharField(max_length=350)
    )
    winner = models.CharField(max_length=50, blank=True)

    def __str__(self):
        name = "{} vs {}".format(self.pokemon_1, self.pokemon_2)
        return name

