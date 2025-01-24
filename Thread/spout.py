import threading
import time

from Models.recipe import Recipe
from Thread.helper import Helper


class Spout(Helper):
    """Class for simulate a helper who pour melt chocolate in mix egg recipe"""
    name: str

    def __init__(self, recipe: Recipe, name):
        super().__init__()
        self.name = name
        self.recipe_helper = recipe
        self.value = 0
        self.lock = threading.Lock()

    def run(self):
        # with self.lock:
        print(f"{self.name}: Je verse du {self.recipe_helper.ingredient}")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f"{self.value} {self.recipe_helper.ingredient.unite}")
