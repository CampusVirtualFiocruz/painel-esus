from abc import ABC, abstractmethod
from src.domain.entities.user_payload import UserPayload

class LoginRepository(ABC):
    @abstractmethod
    def check_credentials(self, username: str, password: str) -> UserPayload: pass
