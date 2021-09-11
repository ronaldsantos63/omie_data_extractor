import requests
import json
import logging

from . import constants
from .exceptions import OmieServiceException, OmieServiceNotFoundException

logger = logging.getLogger(__name__)


class OmieService:

    @staticmethod
    def __post(url: str, payload: str) -> dict:
        try:
            response = requests.post(
                url,
                headers=constants.headers,
                data=payload
            )

            logger.debug(response.url)
            logger.debug("------------> request")
            logger.debug(response.request.headers)
            logger.debug(response.request.body)
            logger.debug("<------------ response")
            logger.debug(response.headers)
            logger.debug(response.json())

            if not response.ok:
                if str(response.text).find("N\\u00e3o existem registros") != -1:
                    raise OmieServiceNotFoundException("Nenhum registro encontrado!")
                raise OmieServiceException(response.text)

            return response.json()
        except Exception as e:
            logger.error(
                f"Ocorreu um erro inesperado no servico: {url}",
                exc_info=True,
                stack_info=True
            )
            raise OmieServiceException(str(e))

    @staticmethod
    def get_nfe_by_period(start_date: str, end_date: str, page: int = 1) -> dict:
        payload = json.dumps({
            "call": "ListarNF",
            "app_key": constants.OMIE_APP_KEY,
            "app_secret": constants.OMIE_APP_SECRET,
            "param": [
                {
                    "pagina": page,
                    "registros_por_pagina": constants.PAGE_SIZE,
                    "ordenar_por": "CODIGO",
                    "tpNF": "1",
                    "dRegInicial": start_date,
                    "dRegFinal": end_date
                }
            ]
        })
        return OmieService.__post(url=f"{constants.BASE_URL}{constants.NFE_RESOURCE}", payload=payload)

    @staticmethod
    def get_sales_order_by_period(start_date: str, end_date: str, page: int = 1) -> dict:
        payload = json.dumps({
            "call": "ListarPedidos",
            "app_key": constants.OMIE_APP_KEY,
            "app_secret": constants.OMIE_APP_SECRET,
            "param": [
                {
                    "pagina": page,
                    "registros_por_pagina": constants.PAGE_SIZE,
                    "ordenar_por": "CODIGO",
                    "filtrar_por_data_de": start_date,
                    "filtrar_por_data_ate": end_date
                }
            ]
        })
        return OmieService.__post(url=f"{constants.BASE_URL}{constants.SALES_ORDER_RESOURCE}", payload=payload)

    @staticmethod
    def get_customer_by_id(customer_id: int) -> dict:
        payload = json.dumps({
            "call": "ConsultarCliente",
            "app_key": constants.OMIE_APP_KEY,
            "app_secret": constants.OMIE_APP_SECRET,
            "param": [
                {
                    "codigo_cliente_omie": customer_id
                }
            ]
        })

        return OmieService.__post(url=f"{constants.BASE_URL}{constants.CUSTOMERS_RESOURCE}", payload=payload)

    @staticmethod
    def get_product_by_cod(product_code: str) -> dict:
        payload = json.dumps({
            "call": "ConsultarProduto",
            "app_key": constants.OMIE_APP_KEY,
            "app_secret": constants.OMIE_APP_SECRET,
            "param": [
                {
                    "codigo_produto": 0,
                    "codigo_produto_integracao": "",
                    "codigo": product_code
                }
            ]
        })

        return OmieService.__post(url=f"{constants.BASE_URL}{constants.PRODUCTS_RESOURCE}", payload=payload)
