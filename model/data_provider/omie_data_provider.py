from datetime import datetime

from service.omie_service import OmieService
from model.data.database_manager import DatabaseManager
from model.data.entity.sales_history_entity import SalesHistoryEntity


class OmieDataProvider:
    __service = OmieService
    __has_data = True
    __database_manager = DatabaseManager()

    def import_sales_history_by_period(self, start_date_str: str, end_date_str: str) -> None:
        current_page = 1
        self.__has_data = True

        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()

        self.__database_manager.delete_by_filter(
            entity=SalesHistoryEntity,
            filter_statement=SalesHistoryEntity.invoice_issue_date.between(start_date, end_date)
        )

        while True:
            if not self.__has_data:
                break
            nfe_result_json = self.__service.get_nfe_by_period(start_date_str, end_date_str, current_page)
            # sales_order_json = self.__service.get_sales_order_by_period(start_date_str, end_date_str, current_page)
            self.__has_data = current_page < nfe_result_json["total_de_paginas"]

            for nf_json in nfe_result_json["nfCadastro"]:
                customer_result_json = self.__service.get_customer_by_id(nf_json["nfDestInt"]["nCodCli"])
                for prod_json in nf_json["det"]:
                    product_info = self.__service.get_product_by_cod(prod_json["prod"]["cProd"])
                    if product_info["descricao_familia"] != "ELANCO":
                        continue
                    sales_history_entity = SalesHistoryEntity.from_json(
                        nf_json,
                        customer_result_json,
                        prod_json["prod"]
                    )

                    self.__database_manager.add(sales_history_entity)
            current_page += 1
        self.__database_manager.close()
