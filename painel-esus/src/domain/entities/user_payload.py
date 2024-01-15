#pylint: disable=invalid-name
#pylint: disable=too-many-arguments
from typing import List
class UserPayload:

    def __init__(
        self,
        username: str,
        cns: str,
        uf: str,
        municipio: str,
        profiles: List[str]
    ) -> None:
        self.username = username
        self.cns = cns
        self.uf = uf
        self.municipio = municipio
        self.profiles = profiles

    def __repr__(self) -> str:
        return f'UserPayload: nome: {self.username}\tcns: {self.cns}'
