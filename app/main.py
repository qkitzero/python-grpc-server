import os
from concurrent import futures

import grpc
from application.tamashii_service import TamashiiService
from infrastructure.tamashii_repository_impl import TamashiiRepositoryImpl
from interface.grpc.tamashii_handler import TamashiiServicer

from pb.tamashii_pb2_grpc import add_TamashiiServiceServicer_to_server


def serve():
    tamashii_repository = TamashiiRepositoryImpl()
    tamashii_service = TamashiiService(tamashii_repository)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_TamashiiServiceServicer_to_server(TamashiiServicer(tamashii_service), server)

    port = os.getenv("PORT")
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
