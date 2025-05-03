from app.application.user_usecase import UserUsecase

from gen.python.proto.user.v1 import user_pb2, user_pb2_grpc


class UserHandler(user_pb2_grpc.UserServiceServicer):
    def __init__(self, user_usecase: UserUsecase):
        self.user_usecase = user_usecase

    def CreateUser(self, request: user_pb2.CreateUserRequest, context):
        user = self.user_usecase.create_user(request.name)
        return user_pb2.CreateUserResponse(id=user.id)

    def GetUser(self, request: user_pb2.GetUserRequest, context):
        user = self.user_usecase.get_user(request.id)
        return user_pb2.GetUserResponse(name=user.name)
