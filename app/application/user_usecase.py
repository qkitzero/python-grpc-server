import uuid

from app.domain.user import User
from app.domain.user_repository_interface import UserRepositoryInterface


class UserUsecase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, name: str) -> User:
        id = str(uuid.uuid4())
        user = User(id, name)
        self.user_repository.create(user)
        return user

    def get_user(self, id: str) -> User:
        user = self.user_repository.read(id)
        return user
