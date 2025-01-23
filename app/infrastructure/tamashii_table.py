from infrastructure.base import Base
from sqlalchemy import VARCHAR, Column


class TamashiiTable(Base):
    __tablename__ = "tamashii"

    id = Column("id", VARCHAR(36), primary_key=True)
    name = Column("name", VARCHAR(100))
