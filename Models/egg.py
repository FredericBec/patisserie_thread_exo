from dataclasses import dataclass

from Models.ingredient import Ingredient


@dataclass
class Egg(Ingredient):
    egg_nb: int

    def __str__(self):
        ingredient_str = super().__str__()
        return f"{ingredient_str} - {self.egg_nb}"
