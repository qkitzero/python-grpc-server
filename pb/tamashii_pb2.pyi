from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTamashiiRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTamashiiResponse(_message.Message):
    __slots__ = ("tamashii_id",)
    TAMASHII_ID_FIELD_NUMBER: _ClassVar[int]
    tamashii_id: str
    def __init__(self, tamashii_id: _Optional[str] = ...) -> None: ...
