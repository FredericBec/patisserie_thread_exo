import math
import time

from Thread.helper import Helper
from Models.chocolate import Chocolate


class MeltingChocolate(Helper):
    def __int__(self, chocolate: Chocolate):
        self.quantity = chocolate.quantity

    def run(self):
        print("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print("Je verse l'eau dans une casserole")
        time.sleep(2)
        print("J'y pose le bol rempli de chocolat")
        time.sleep(1)

        nb_turns = math.ceil(self.quantity / 10)
        for nb_turn in range(1, nb_turns + 1):
            print(f"Je mélange {self.quantity} de chocolat à fondre, tour n°{nb_turn}")
            time.sleep(1)