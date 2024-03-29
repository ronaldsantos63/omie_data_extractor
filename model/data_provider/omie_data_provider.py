import logging
from datetime import datetime
from typing import Optional

from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from model.data.entity.products_entity import ProductEntity
from model.data.entity.sellers_entity import SellersEntity
from service.omie_service import OmieService
from model.data.database_manager import DatabaseManager
from model.data.entity.sales_history_entity import SalesHistoryEntity


class OmieDataProvider:
    __logger = logging.getLogger(__name__)
    __service = OmieService

    def import_sales_history_by_period(self, start_date_str: str, end_date_str: str,
                                       check_products_in_local_database=False) -> None:
        database_manager = DatabaseManager()
        current_page = 1
        __has_data = True

        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()

        database_manager.delete_by_filter(
            entity=SalesHistoryEntity,
            filter_statement=SalesHistoryEntity.invoice_issue_date.between(start_date, end_date)
        )

        while True:
            if not __has_data:
                break
            nfe_result_json = self.__service.get_nfe_by_period(start_date_str, end_date_str, current_page)
            # sales_order_json = self.__service.get_sales_order_by_period(start_date_str, end_date_str, current_page)
            __has_data = current_page < nfe_result_json["total_de_paginas"]

            for nf_json in nfe_result_json["nfCadastro"]:
                if nf_json['ide'].get('cDeneg') == 'S':
                    continue
                seller_omie_id = nf_json['pedido'].get('nIdVendedor')
                seller_entity = self.__get_seller(
                    seller_omie_id=seller_omie_id,
                    database_manager=database_manager
                )
                customer_result_json = self.__service.get_customer_by_id(nf_json["nfDestInt"]["nCodCli"])
                for prod_json in nf_json["det"]:
                    is_elanco_product = self.__is_elanco_product(
                            check_products_in_local_database=check_products_in_local_database,
                            prod_json=prod_json,
                            database_manager=database_manager
                    )
                    if not is_elanco_product:
                        continue

                    sales_history_entity = SalesHistoryEntity.from_json(
                        nf_json,
                        customer_result_json,
                        prod_json,
                        seller_entity
                    )

                    database_manager.add(sales_history_entity)
            current_page += 1
        database_manager.close()

    def __is_elanco_product(
            self,
            check_products_in_local_database,
            prod_json,
            database_manager: DatabaseManager
    ) -> bool:
        if check_products_in_local_database:
            product_database_result = database_manager.get_by_filter(
                ProductEntity, ProductEntity.gtin == prod_json["prod"]["cProd"]
            )
            return product_database_result.count() > 0
        else:
            product_info = self.__service.get_product_by_cod(prod_json["prod"]["cProd"])
            return product_info["descricao_familia"] == "ELANCO"

    def __get_seller(self, seller_omie_id: Optional[int], database_manager: DatabaseManager) -> Optional['SellersEntity']:
        try:
            if not seller_omie_id:
                return None
            seller_entity = database_manager.get_by_filter(
                entity=SellersEntity,
                filter_statement=SellersEntity.id_omie == seller_omie_id
            ).one()
            return seller_entity
        except MultipleResultsFound:
            self.__logger.log(
                f'A busca pelo vendedor {seller_omie_id} retornou mais de um registro!',
                exc_info=True,
                stack_info=True
            )
            return None
        except NoResultFound:
            self.__logger.log(
                f'Não foi encontrado nenhum vendedor com o id {seller_omie_id}',
                exc_info=True,
                stack_info=True
            )
            return None

    def import_products(self, filters: dict = None):
        database_manager = DatabaseManager()
        current_page = 1
        __has_data = True
        database_manager.delete_all(ProductEntity)
        while __has_data:
            products_json = self.__service.get_products(current_page, filters)
            __has_data = current_page < products_json["total_de_paginas"]

            for product_json in products_json["produto_servico_cadastro"]:
                product_entity = ProductEntity.from_json(product_json)
                database_manager.add(product_entity)
            current_page += 1
        database_manager.close()

    def import_sellers(self):
        database_manager = DatabaseManager()
        current_page = 1
        __has_data = True
        database_manager.delete_all(SellersEntity)
        while __has_data:
            sellers_json = self.__service.get_sellers(current_page)
            __has_data = current_page < sellers_json['total_de_paginas']

            for seller_json in sellers_json['cadastro']:
                seller_entity = SellersEntity.from_json(seller_json)
                database_manager.add(seller_entity)
            current_page += 1
        database_manager.close()
