import time

from Models.recipe import Recipe
from Thread.helper import Helper


class MeltingChocolate(Helper):
    name: str

    def __init__(self, recipe: Recipe, name):
        super().__init__()
        self.name = name
        self.recipe_helper = recipe

    def run(self):
        print(f"{self.name}: Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print(f"{self.name}: Je verse l'eau dans une casserole")
        time.sleep(2)
        print(f"{self.name}: J'y pose le bol rempli de chocolat")
        time.sleep(1)

        self.recipe_helper.melt(self.name)
