import math
import time
from dataclasses import dataclass

from Services.appliance import Appliance
from Models.chocolate import Chocolate
from Models.egg import Egg


@dataclass
class Recipe:
    """
    Class recipe with two method in function of ingredient
    """
    appliance: Appliance
    ingredient: Egg | Chocolate

    def melt(self, name: str):
        """Method for simulate melting chocolate"""
        nb_turns = math.ceil(self.ingredient.quantity / 10)
        for nb_turn in range(1, nb_turns + 1):
            print(f"{name} Je mélange {self.ingredient.quantity} de chocolat à fondre, tour n°{nb_turn}")
            time.sleep(1)

    def bake(self, name: str):
        """Method for simulate mixing eggs"""
        nb_turns = self.ingredient.quantity * 8
        for nb_turn in range(1, nb_turns + 1):
            print(f"\t{name}: Je bats les {self.ingredient.quantity} oeufs, tour n°{nb_turn}")
            time.sleep(0.5)
