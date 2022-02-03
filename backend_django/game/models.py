from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Battle(models.Model):
    # TODO: foreignkey for user that ran the battle
    pokemon_1 = models.CharField(max_length=50)
    pokemon_2 = models.CharField(max_length=50)
    move_log = ArrayField(
        models.CharField(max_length=350)
    )
    winner = models.CharField(max_length=50, blank=True)

    def __str__(self):
        name = "{} vs {}".format(self.pokemon_1, self.pokemon_2)
        return name

