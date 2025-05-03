from domain.user import User
from domain.user_repository_interface import UserRepositoryInterface
from sqlalchemy.orm import Session

from app.infrastructure.user_table import UserTable


class UserRepositoryImpl(UserRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> None:
        user_table = UserTable(id=user.id, name=user.name)
        self.session.add(user_table)
        self.session.commit()

    def read(self, id: str) -> User:
        user_table = self.session.query(UserTable).filter_by(id=id).first()
        return User(user_table.id, user_table.name)
