from abc import ABC, abstractmethod

from domain.tamashii import Tamashii


class TamashiiRepositoryInterface(ABC):
    @abstractmethod
    def create(self, tamashii: Tamashii) -> None:
        pass

    @abstractmethod
    def read(self, id: str) -> Tamashii:
        pass
