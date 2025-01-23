import uuid

from domain.tamashii import Tamashii
from domain.tamashii_repository_interface import TamashiiRepositoryInterface


class TamashiiService:
    def __init__(self, tamashii_repository: TamashiiRepositoryInterface):
        self.tamashii_repository = tamashii_repository

    def create_tamashii(self, name: str) -> Tamashii:
        id = str(uuid.uuid4())
        tamashii = Tamashii(id, name)
        self.tamashii_repository.create(tamashii)
        return tamashii

    def get_tamashii(self, id: str) -> Tamashii:
        tamashii = self.tamashii_repository.read(id)
        return tamashii
