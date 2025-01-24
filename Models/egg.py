from dataclasses import dataclass

from Models.ingredient import Ingredient


@dataclass
class Egg(Ingredient):
    """Class extend ingredient"""

    def __str__(self):
        ingredient_str = super().__str__()
        return f"{ingredient_str}"
