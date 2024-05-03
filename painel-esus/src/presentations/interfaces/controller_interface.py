from abc import ABC, abstractmethod

from src.presentations.http_types import HttpRequest, HttpResponse


class ControllerInterface(ABC):

    @abstractmethod
    def handle(self, request: HttpRequest) -> HttpResponse: pass
