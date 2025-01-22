from domain.tamashii import Tamashii
from domain.tamashii_repository import TamashiiRepository


class TamashiiService:
    def __init__(self, tamashii_repository: TamashiiRepository):
        self.tamashii_repository = tamashii_repository

    def create_tamashii(self, name: str) -> Tamashii:
        tamashii = Tamashii("1", name)
        self.tamashii_repository.create(tamashii)
        return tamashii

    def get_tamashii(self, id: str) -> Tamashii:
        tamashii = self.tamashii_repository.read(id)
        return tamashii
