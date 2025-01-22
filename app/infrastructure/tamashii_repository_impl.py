from domain.tamashii import Tamashii
from domain.tamashii_repository import TamashiiRepository


class TamashiiRepositoryImpl(TamashiiRepository):
    def __init__(self):
        self.db = "db"

    def create(self, tamashii: Tamashii) -> None:
        pass

    def read(self, id: str) -> Tamashii:
        return Tamashii(id, "name")
