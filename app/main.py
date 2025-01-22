import os
from concurrent import futures
import grpc
from pb import tamashii_pb2_grpc
import interface.grpc.tamashii.handler


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tamashii_pb2_grpc.add_TamashiiServiceServicer_to_server(interface.grpc.tamashii.handler.TamashiiServicer(), server)
    port = os.getenv('PORT')
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()