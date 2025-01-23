from Models.recipe import Recipe
from Thread.helper import Helper


class BeatEgg(Helper):
    def __init__(self, recipe: Recipe):
        super().__init__()
        self.recipe_helper = recipe

    def run(self):
        self.recipe_helper.bake()
