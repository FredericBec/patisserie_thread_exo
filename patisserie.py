import concurrent.futures
import threading
import time
import math

from Models.chocolate import Chocolate
from Models.egg import Egg
from Models.recipe import Recipe
from Services.appliance import Appliance
from Thread.beatEgg import BeatEgg
from Thread.meltingChocolate import MeltingChocolate
from Thread.spout import Spout


class BatteurOeufs(threading.Thread):
    def __init__(self, nb_oeufs):
        threading.Thread.__init__(self)
        self.nb_oeufs = nb_oeufs

    def run(self):
        # on suppose qu'il faut 8 tours de batteur par œuf présent dans le bol
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\tJe bats les {self.nb_oeufs} oeufs, tour n°{no_tour}")
            time.sleep(0.5)  # temps supposé d'un tour de batteur


class FondeurChocolat(threading.Thread):
    def __init__(self, quantite):
        threading.Thread.__init__(self)
        self.quantite = quantite  # en grammes

    def run(self):
        print("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print("Je verse l'eau dans une casserole")
        time.sleep(2)
        print("J'y pose le bol rempli de chocolat")
        time.sleep(1)
        # on suppose qu'il faut 1 tour de spatule par 10 g. de chocolat
        # présent dans le bol pour faire fondre le chocolat
        nb_tours = math.ceil(self.quantite / 10)
        for no_tour in range(1, nb_tours + 1):
            print(f"Je mélange {self.quantite} de chocolat à fondre, tour n°{no_tour}")
            time.sleep(1)  # temps supposé d'un tour de spatule


def bake_cake():
    chocolate = Chocolate("Chocolat noir", 200, "grammes")
    egg = Egg("Oeufs", 6, "unité")
    kettle = Appliance()
    egg_beater = Appliance()
    recipe_chocolate = Recipe(kettle, chocolate)
    recipe_egg = Recipe(egg_beater, egg)
    chocolate_helper = MeltingChocolate(recipe_chocolate, "Fondeur de chocolat")
    bake_helper = BeatEgg(recipe_egg, "Batteur d'oeufs")
    first_spout_helper = Spout(recipe_chocolate, "Verseur 1")
    second_spout_helper = Spout(recipe_chocolate, "Verseur 2")
    bake_helper.start()
    chocolate_helper.start()
    bake_helper.join()
    chocolate_helper.join()
    print("\nJe peux à présent incorporer le chocolat aux oeufs")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for _ in range(recipe_chocolate.ingredient.quantity):
            executor.submit(first_spout_helper.run)
            executor.submit(second_spout_helper.run)


if __name__ == "__main__":
    bake_cake()

