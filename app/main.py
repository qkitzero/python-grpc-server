import os
from concurrent import futures

import grpc
from app.application.user_usecase import UserUsecase
from infrastructure.db import setup_engine
from app.infrastructure.user_repository import UserRepositoryImpl
from app.interface.grpc.user_handler import UserHandler
from sqlalchemy.orm import Session, sessionmaker

from gen.python.proto.user.v1 import user_pb2_grpc


def serve():
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    engine = setup_engine(db_user, db_password, db_host, db_port, db_name)

    SessionClass = sessionmaker(engine)
    session = SessionClass()

    user_repository = UserRepositoryImpl(session)
    user_usecase = UserUsecase(user_repository)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    user_pb2_grpc.add_UserServiceServicer_to_server(UserHandler(user_usecase), server)

    port = os.getenv("PORT")
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
