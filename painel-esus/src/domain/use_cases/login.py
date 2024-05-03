from abc import ABC, abstractmethod
from src.domain.entities.user_payload import UserPayload

class LoginUseCase(ABC):
    @abstractmethod
    def login(self, username: str, password: str) -> UserPayload: pass
