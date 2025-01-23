from domain.tamashii import Tamashii
from domain.tamashii_repository_interface import TamashiiRepositoryInterface
from infrastructure.tamashii_table import TamashiiTable
from sqlalchemy.orm import Session


class TamashiiRepositoryImpl(TamashiiRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def create(self, tamashii: Tamashii) -> None:
        tamashii_table = TamashiiTable(id=tamashii.id, name=tamashii.name)
        self.session.add(tamashii_table)
        self.session.commit()

    def read(self, id: str) -> Tamashii:
        tamashii_table = self.session.query(TamashiiTable).filter_by(id=id).first()
        return Tamashii(tamashii_table.id, tamashii_table.name)
