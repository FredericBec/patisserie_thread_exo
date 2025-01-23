import threading
import time

from Models.recipe import Recipe
from Thread.helper import Helper


class Spout(Helper):
    def __init__(self, recipe: Recipe):
        super().__init__()
        self.recipe_helper = recipe
        self.value = 0
        self.lock = threading.Lock()

    def run(self):
        with self.lock:
            print(f"Je verse du {self.recipe_helper.ingredient}")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.5)
            self.value = local_copy
            print(f"{self.value}")
