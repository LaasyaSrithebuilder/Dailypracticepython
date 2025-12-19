from abc import ABC,abstractmethod
from vechile import Vechile

class MiantanenceTool(ABC):
    @abstractmethod
    def perform_maintanence(self,vechile:Vechile):
        pass