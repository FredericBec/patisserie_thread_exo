from dataclasses import dataclass

from Services.appliance import Appliance
from Models.chocolate import Chocolate
from Models.egg import Egg


@dataclass
class Recipe:
    appliance: Appliance
    ingredient: Egg | Chocolate
