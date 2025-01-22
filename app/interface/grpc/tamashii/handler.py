from pb import tamashii_pb2, tamashii_pb2_grpc


class TamashiiServicer(tamashii_pb2_grpc.TamashiiServiceServicer):
    def CreateTamashii(self, request, context):
        return tamashii_pb2.CreateTamashiiResponse(tamashii_id="tamashii id")
