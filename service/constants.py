from PyQt5.QtCore import QSettings

__settings = QSettings("Ronald Santos", "OMIE Data Extractor")

BASE_URL = "https://app.omie.com.br/api/v1/"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# PAGE_SIZE = 20
#
# OMIE_APP_KEY = "1343719989612"
# OMIE_APP_SECRET = "ac8750f63291de4003e7deae489c29bc"

PAGE_SIZE = __settings.value("omie_page_size", defaultValue=20, type=int)
OMIE_APP_KEY = __settings.value("omie_app_key", defaultValue="", type=str)
OMIE_APP_SECRET = __settings.value("omie_app_secret", defaultValue="", type=str)

# Resources
NFE_RESOURCE = "produtos/nfconsultar/"
SALES_ORDER_RESOURCE = "produtos/pedido/"
CUSTOMERS_RESOURCE = "geral/clientes/"
PRODUCTS_RESOURCE = "geral/produtos/"
