import os
from concurrent import futures

import grpc
from application.tamashii_service import TamashiiService
from infrastructure.db import setup_engine
from infrastructure.tamashii_repository import TamashiiRepositoryImpl
from interface.grpc.tamashii_handler import TamashiiServicer
from sqlalchemy.orm import Session, sessionmaker

from pb.tamashii_pb2_grpc import add_TamashiiServiceServicer_to_server


def serve():
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    engine = setup_engine(db_user, db_password, db_host, db_port, db_name)

    SessionClass = sessionmaker(engine)
    session = SessionClass()

    tamashii_repository = TamashiiRepositoryImpl(session)
    tamashii_service = TamashiiService(tamashii_repository)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_TamashiiServiceServicer_to_server(TamashiiServicer(tamashii_service), server)

    port = os.getenv("PORT")
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
