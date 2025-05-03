from abc import ABC, abstractmethod

from app.domain.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: User) -> None:
        pass

    @abstractmethod
    def read(self, id: str) -> User:
        pass
