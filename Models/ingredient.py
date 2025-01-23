from abc import ABC
from dataclasses import dataclass

@dataclass
class Ingredient(ABC):
    name: str
    quantity: float
    unite: str

    def __str__(self) -> str:
        return f"{self.name} - {self.quantity} {self.unite}"
