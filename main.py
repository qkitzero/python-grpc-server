import os
from concurrent import futures
import grpc
from pb import tamashii_pb2
from pb import tamashii_pb2_grpc


class TamashiiServicer(tamashii_pb2_grpc.TamashiiServiceServicer):
    def CreateTamashii(self, request, context):
        return tamashii_pb2.CreateTamashiiResponse(tamashii_id="tamashii id")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tamashii_pb2_grpc.add_TamashiiServiceServicer_to_server(TamashiiServicer(), server)
    port = os.getenv('PORT')
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()