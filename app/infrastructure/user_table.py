from infrastructure.base import Base
from sqlalchemy import VARCHAR, Column


class UserTable(Base):
    __tablename__ = "user"

    id = Column("id", VARCHAR(36), primary_key=True)
    name = Column("name", VARCHAR(100))
