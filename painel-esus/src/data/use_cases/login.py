from src.domain.use_cases.login import LoginUseCase as LoginUseCaseInterface
from src.domain.entities.user_payload import UserPayload
from src.data.interfaces.login_repository import LoginRepository
from src.errors import (
    InvalidArgument,
    HttpCredentialsFailError,
    HttpBadRequestError
)


class LoginUseCase(LoginUseCaseInterface):

    def __init__(self, repository: LoginRepository):
        self.__repository = repository

    @classmethod
    def __validate_username(cls, username: str) -> None:
        if not username or not isinstance(username, str):
            raise InvalidArgument('Username is required and must be string.')

        if len(username) <= 3:
            raise HttpBadRequestError('Username too short')

    @classmethod
    def __validate_password(cls, password: str) -> None:
        if not password or not isinstance(password, str):
            raise InvalidArgument('Password is required and must be string.')

        if len(password) <= 3:
            raise HttpBadRequestError('Password too short')

    def login(self, username: str, password: str) -> UserPayload:
        self.__validate_username(username)
        self.__validate_password(password)

        user_raw_data = self.__repository.check_credentials(
            username=username,
            password=password
        )
        if not user_raw_data:
            raise HttpCredentialsFailError('Credentials fail.')
        return user_raw_data
