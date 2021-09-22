from sqlalchemy import Column, Integer, BigInteger, String

from model.data import mapper_registry


@mapper_registry.mapped
class SellersEntity:
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True)
    id_omie = Column(BigInteger, nullable=False, index=True)
    inactive = Column(String(1))
    name = Column(String(500), nullable=False, index=True)

    @staticmethod
    def from_json(seller_json: dict) -> 'SellersEntity':
        return SellersEntity(
            id_omie=seller_json['codigo'],
            inactive=seller_json['inativo'],
            name=seller_json['nome']
        )

