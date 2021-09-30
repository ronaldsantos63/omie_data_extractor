# OMIE Data Extractor
Este projeto foi desenvolvido com a finalidade de apenas extrair dados do sistema OMIE para um banco de dados local para realizar a integração entre a OMIE e a empresa Elanco

## Dependências
- Git
- Python 3.9
- Pipenv

## Como excutar?
1. clonar o repositório
   > $ git clone git@github.com:ronaldsantos63/omie_data_extractor.git
2. Entrar na pasta do repositório clonado
   > $ cd omie_data_extractor
3. Executar o seguinte comando para instalar as libs
   > $ pipenv install
4. Executar o seguinte comando para instalar as libs de dev
   > $ pipenv install -d
5. Executar o projeto
   > $ pipenv run python omie_data_extractor.py

## Como criar executavel?
Executar o script setup.bat(apenas para windows)
> $ setup.bat

## Como configurar?
1. Pegar as credências **APP Key** e **App Secret** da API no site [OMIE Developer](https://developer.omie.com.br/my-apps/)
2. Pegar o id da família de produtos da Elanco com o seu cliente
3. Importar produtos filtrando pelo id da familia
4. Importar os vendedores
5. Importar as vendas filtrando pela data inicial e final
6. Deixar marcado o checkbox **Verificar produtos Elanco na base Local** para otimizar as consultas via api!
7. No software de integração da Elanco configure para ler o banco de dados criado pelo **OMIE Data Extractor**

### Fotos
![OMIE Data extractor](https://i.ibb.co/Hp3gQjG/Captura-de-Tela-2021-09-29-a-s-21-49-43.png)