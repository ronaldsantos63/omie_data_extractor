from sqlalchemy import Column, Integer, String

from model.data import mapper_registry


@mapper_registry.mapped
class ProductEntity:
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    id_omie = Column(String, nullable=False, index=True)
    gtin = Column(String(50), nullable=False, index=True)
    ean = Column(String(20), nullable=False, index=True)
    description = Column(String(500), nullable=False, index=True)
    family_description = Column(String(500), nullable=False, default='', index=True)

    @staticmethod
    def from_json(product_json: dict) -> 'ProductEntity':
        return ProductEntity(
            id_omie=product_json['codigo_produto'],
            gtin=product_json['codigo'],
            ean=product_json['ean'],
            description=product_json['descricao'],
            family_description=product_json['descricao_familia']
        )
