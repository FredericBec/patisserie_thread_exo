import time

from Models.recipe import Recipe
from Thread.helper import Helper


class MeltingChocolate(Helper):
    def __init__(self, recipe: Recipe):
        super().__init__()
        self.recipe_helper = recipe

    def run(self):
        print("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print("Je verse l'eau dans une casserole")
        time.sleep(2)
        print("J'y pose le bol rempli de chocolat")
        time.sleep(1)

        self.recipe_helper.melt()
