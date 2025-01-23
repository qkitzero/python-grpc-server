from infrastructure.base import Base
from sqlalchemy import create_engine


def setup_engine(user: str, password: str, host: str, port: str, name: str):
    url = (
        f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{name}?charset=utf8mb4"
    )
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    return engine
