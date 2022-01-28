from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


# class Move(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     pp = models.PositiveIntegerField()
#     accuracy = models.PositiveIntegerField()
#     power = models.PositiveIntegerField()

#     def __str__(self) -> str:
#         return self.name

#     def useMove(self):
#         if (self.pp > 0):
#             self.pp -= 1

#     def is_available(self):
#         if (self.pp > 0):
#             return True
#         else:
#             return False


# class Pokemon(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     hp = models.PositiveIntegerField(default=100)
#     moves = models.ManyToManyField(Move, related_name='pokemon')

#     def __str__(self) -> str:
#         return self.name


class Battle(models.Model):
    pokemon_1 = models.CharField(max_length=50)
    pokemon_2 = models.CharField(max_length=50)
    move_log = ArrayField(
        models.CharField(max_length=250)
    )
    winner = models.CharField(max_length=50)

    def __str__(self):
        name = "{} vs {}".format(self.pokemon_1, self.pokemon_2)
        return name

