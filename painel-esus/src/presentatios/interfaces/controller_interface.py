from abc import ABC, abstractmethod
from src.presentatios.http_types import HttpResponse, HttpRequest

class ControllerInterface(ABC):

    @abstractmethod
    def handle(self, request:HttpRequest) -> HttpResponse: pass
