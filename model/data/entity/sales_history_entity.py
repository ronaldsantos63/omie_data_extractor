from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Date

from model.data import mapper_registry
from model.data.entity.sellers_entity import SellersEntity


@mapper_registry.mapped
class SalesHistoryEntity:
    __tablename__ = "sales_history"

    id = Column(Integer, primary_key=True)
    cnpj_cpf = Column(String(14), nullable=False, index=True)
    state_registration = Column(String(20), nullable=True, default="", comment="Será utilizado para identificar "
                                                                               "clientes pessoa "
                                                                               "Física que possuam diferentes "
                                                                               "propriedades "
                                                                               "rurais.")
    client_name = Column(String(200), nullable=False, index=True)
    customer_grouping = Column(String(80), nullable=True, default="", comment="Neste campo poderá ser inserido o "
                                                                              "agrupamento do cliente, isto é, "
                                                                              "um nome ou uma sigla que poderemos "
                                                                              "agrupar alguns clientes.")
    cep = Column(String(20), nullable=False)
    uf = Column(String(2), nullable=False, comment="Estado do cliente, utilizando 2 dígitos conforme estados da "
                                                   "federação.")
    city = Column(String(100), nullable=False)
    address = Column(String, nullable=True, default="", comment="Endereço, (vírgula)Número, (vírgula)Complemento,"
                                                                "(vírgula) Bairro.")
    telephone = Column(String(20), nullable=True, default="", comment="(DDD) XXXX-XXXX")
    email = Column(String(100), nullable=True, default="")
    transaction_date = Column(String(20), nullable=False, comment="A data terá o formato “ddmmaaaa”, onde: - dd: dia "
                                                                  "da operação; - mm: mês da operação; - aaaa: ano da"
                                                                  " operação.")
    product_code = Column(String(20), nullable=False, comment="Código atribuído pelo distribuidor ao produto Elanco.")
    quantity = Column(Integer, nullable=False, comment="Quantidade vendida do produto, aceitos somente números e "
                                                       "inteiros.")
    total_price = Column(String(20), nullable=False, comment="Valor (preço) total da quantidade vendida de cada "
                                                             "produto. Numérico com 2 casas decimais. Valor = Preço "
                                                             "do Produto vendido x Quantidade Vendida")
    sales_zone_code = Column(String(20), nullable=True, default="", comment="Neste campo deverá ser inserido o código "
                                                                            "da zona de venda do distribuidor.")
    sales_zone_description = Column(String, nullable=False, default="", comment="Neste campo deverá ser inserida a "
                                                                                "zona de venda do distribuidor.")
    bu = Column(String(80), nullable=True, default="", comment="Uma classificação do cliente com relação a "
                                                               "representatividade do mesmo. Por exemplo: uma "
                                                               "agropecuária revende produtos de bovinos e de pet, "
                                                               "qual destas duas linhas de produtos é mais vendida "
                                                               "por ela ? Se for bovinos, a BU deste cliente será "
                                                               "BOVINOS, caso contrário será CA. Valores aceitos: "
                                                               "BOVINOS AVES, SUÍNOS, AVES E SUÍNOS, AQUA, CA, "
                                                               "CAPRINOS, EQUINOS, OUTROS")
    classification = Column(String(80), nullable=False, comment="Classificação da Operação da Venda será conforme "
                                                                "domínio. EMPRÉSTIMO: deverá se utilizada quando há "
                                                                "um empréstimo de produto para alguém, "
                                                                "seja este alguém um cliente ou até mesmo um "
                                                                "empréstimo para outro distribuidor. DEVOLUÇÃO "
                                                                "EMPRÉSTIMO: deverá ser utilizado quando há a "
                                                                "devolução de um empréstimo, seja esta devolução "
                                                                "vinda do cliente ou até mesmo de um outro "
                                                                "distribuidor. Obs.: as classificações de devolução "
                                                                "que deverão ser consideradas serão somente as "
                                                                "devoluções ocorridas entre o distribuidor e seus "
                                                                "clientes. Isto é, não deverão ser consideradas as "
                                                                "devoluções ocorridas do distribuidor para a Elanco. "
                                                                "Valores aceitos: VENDA DEVOLUCAO, BONIFICACAO, "
                                                                "AMOSTRA, TESTE, LICITACAO, VENDA INTERNA, "
                                                                "INCINERACAO, RECALL, CANCELAMENTO, ALTERAÇAO, "
                                                                "EMPRESTIMO, DEVOLUÇÃO EMPRÉSTIMO, OUTROS")
    first_additional_field = Column(String, nullable=True, default="", comment="Este campo deve ser enviado no "
                                                                               "arquivo, porém vazio, ou seja, "
                                                                               "sem preenchimento, "
                                                                               "separado apenas por ';'")
    second_additional_field = Column(String, nullable=True, default="", comment="Este campo deve ser enviado no "
                                                                                "arquivo, porém vazio, ou seja, "
                                                                                "sem preenchimento, "
                                                                                "separado apenas por ';'")
    type_of_store = Column(String(100), nullable=False, default="DISTRIBUIDOR", comment="Classificação do cliente com "
                                                                                        "base nas opções ao lado "
                                                                                        "(usar o mesmo texto). Não "
                                                                                        "utilizar acentos, "
                                                                                        "espaços e caracteres "
                                                                                        "especiais. Valores aceitos: "
                                                                                        "AGROINDUSTRIA, ATACADO, "
                                                                                        "CLINICA VETERINARIA, "
                                                                                        "COOPERATIVA, DISTRIBUIDOR, "
                                                                                        "ECOMMERCE, "
                                                                                        "FAZENDA e PRODUTOR RURAL, "
                                                                                        "PESSOA FISICA, PET SHOP, "
                                                                                        "PET SHOP e CLINICA "
                                                                                        "VETERINARIA, PREMIXEIRA, "
                                                                                        "REVENDA.")
    pigs = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores da unidade "
                                                             "Aves e Suínos.")
    piglets = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores da "
                                                                "unidade Aves e Suínos.")
    birds = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores da "
                                                              "unidade Aves e Suínos.")
    poedeiras = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores da "
                                                                  "unidade Aves e Suínos.")
    chicken = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores da "
                                                                "unidade Aves e Suínos.")
    cameroon = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores da "
                                                                 "unidade Aqua.")
    pisces = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores da "
                                                               "unidade Aqua.")
    bovine = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores das "
                                                               "unidades Gado de Leite e Gado de Corte.")
    cow = Column(String, nullable=True, default="", comment="Serão preenchidos somente por distribuidores das "
                                                            "unidades Gado de Leite e Gado de Corte.")
    lot = Column(String, nullable=True, default="", comment="Numero de lote Elanco do produto vendido")
    invoice_number = Column(Integer, nullable=False, comment="Numero da nota fiscal")
    invoice_issue_date = Column(Date, nullable=False, index=True, comment="A data terá o formato “ddmmaaaa”, "
                                                                          "onde: - dd: "
                                                                          "dia da operação; - mm: mês da "
                                                                          "operação; - aaaa: "
                                                                          "ano da operação.")
    cfop = Column(String(5), nullable=False)

    @staticmethod
    def from_json(
            nfe_json_dict: dict,
            customer_json_dict: dict,
            product_json_dict: dict,
            seller_entity: Optional['SellersEntity']
    ) -> "SalesHistoryEntity":

        def get_classification_name_by_cfop(cfop) -> str:
            if cfop in ["5102", "6102", "5103", "6103", "5104", "6104", "5120", "6120", "5401", "6401", "5402", "6402",
                        "5403", "6403", "5405"]:
                return "VENDA"
            elif cfop in ["5910", "6910"]:
                return "BONIFICACAO"
            elif cfop in ["1200", "1202", "1203", "1204", "1410", "1411", "5202", "6202"]:
                return "DEVOLUCAO"

        if nfe_json_dict["ide"]["dInut"] != "" or nfe_json_dict["ide"]["dCan"] != "":
            classification = "CANCELAMENTO"
        else:
            classification = get_classification_name_by_cfop(str(product_json_dict["CFOP"]).replace(".", ""))

        date_str = nfe_json_dict["ide"]["dCan"] if nfe_json_dict["ide"]["dCan"] != "" else \
            nfe_json_dict["ide"]["dInut"] if nfe_json_dict["ide"]["dInut"] != "" else nfe_json_dict["ide"]["dEmi"]

        date = datetime.strptime(date_str, "%d/%m/%Y")

        return SalesHistoryEntity(
            cnpj_cpf=str(customer_json_dict["cnpj_cpf"]).replace(".", "").replace("/", "").replace("-", ""),
            state_registration=customer_json_dict.get("inscricao_estadual", "").upper().replace("ISENTO", "")
                .replace("-", "")
                .replace(".", "")
                .replace("/", ""),
            client_name=customer_json_dict["razao_social"],
            cep=customer_json_dict["cep"],
            uf=customer_json_dict["estado"],
            city=customer_json_dict["cidade"],
            address=f"{str(customer_json_dict['endereco']).replace(',', ' ').replace('-', ' ')},"
                    f"{str(customer_json_dict['endereco_numero']).replace('S-N', 'SN').replace(' ', '')},"
                    f"{customer_json_dict['complemento']},{customer_json_dict['bairro']}",
            telephone=f"({customer_json_dict['telefone1_ddd']}) {customer_json_dict['telefone1_numero']}",
            email=customer_json_dict["email"],
            transaction_date=date.strftime("%d%m%Y"),
            product_code=product_json_dict["cProd"],
            quantity=product_json_dict["qCom"],
            total_price=f"{product_json_dict['vTotItem'] - product_json_dict['vDesc']:.2f}".replace('.', ','),
            classification=classification,
            invoice_number=int(nfe_json_dict["ide"]["nNF"]),
            invoice_issue_date=date.date(),
            cfop=str(product_json_dict["CFOP"]).replace(".", ""),
            sales_zone_code=seller_entity.id_omie if seller_entity else '',
            sales_zone_description=seller_entity.name if seller_entity else ''
        )
