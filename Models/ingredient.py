from abc import ABC
from dataclasses import dataclass


@dataclass
class Ingredient(ABC):
    """Abstract class ingredient"""
    name: str
    quantity: int
    unite: str

    def __str__(self) -> str:
        return f"{self.name} - {self.quantity} {self.unite}"
