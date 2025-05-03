from app.application.user_usecase import UserService

from pb import user_pb2, user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServiceServicer):
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def CreateUser(self, request: user_pb2.CreateUserRequest, context):
        user = self.user_service.create_user(request.name)
        return user_pb2.CreateUserResponse(id=user.id)

    def GetUser(self, request: user_pb2.GetUserRequest, context):
        user = self.user_service.get_user(request.id)
        return user_pb2.GetUserResponse(name=user.name)
