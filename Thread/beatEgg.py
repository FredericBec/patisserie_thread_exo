from Models.recipe import Recipe
from Thread.helper import Helper


class BeatEgg(Helper):
    name: str

    def __init__(self, recipe: Recipe, name):
        super().__init__()
        self.name = name
        self.recipe_helper = recipe

    def run(self):
        self.recipe_helper.bake(self.name)
