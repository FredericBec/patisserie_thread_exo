import threading
from abc import ABC, abstractmethod


class Helper(threading.Thread, ABC):
    """Abstract thread class"""

    def __int__(self, *args):
        super().__init__(*args)

    @abstractmethod
    def run(self):
        """abstract method for threading"""
        pass



