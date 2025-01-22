from application.tamashii_service import TamashiiService

from pb import tamashii_pb2, tamashii_pb2_grpc


class TamashiiServicer(tamashii_pb2_grpc.TamashiiServiceServicer):
    def __init__(self, tamashii_service: TamashiiService):
        self.tamashii_service = tamashii_service

    def CreateTamashii(self, request: tamashii_pb2.CreateTamashiiRequest, context):
        tamashii = self.tamashii_service.create_tamashii(request.name)
        return tamashii_pb2.CreateTamashiiResponse(id=tamashii.id)

    def GetTamashii(self, request: tamashii_pb2.GetTamashiiRequest, context):
        tamashii = self.tamashii_service.get_tamashii(request.id)
        return tamashii_pb2.GetTamashiiResponse(name=tamashii.name)
