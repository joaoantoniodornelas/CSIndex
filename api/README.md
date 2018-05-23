
# API REST - CSIndex
Trabalho prático de Engenharia de Software 2.

## Autor

João Antônio Dornelas Orlando Netto - 2014103407

## Objetivo

O objetivo dessa API é facilitar a busca de dados no banco de Indexação da produção ciêntífica em Ciência da Computação no Brasil (CSIndex). As consultas permitem o retorno de autores, publicações, departamentos, conferências e áreas do conhecimento

## Implementação

Linguagem: python 2.7
Bibliotecas utilizadas: Nesse projeto, foram utilizadas duas bibliotecas terceiras, para facilitar o desenvolvimento da API e a manipulação de dados:
* Flask: Biblioteca Python para desenvolvimento de aplicações Web, capaz de lidar com respostas, controle de caches, cookies, status HTTP, entre outros. Foi a biblioteca principal para o desenvolvimento da API REST proposta para esse trabalho. Para instalação, execute o comando "pip install Flask"
* Pandas: Biblioteca para manipulação de dados, com recursos avançados de indexação e criação de bancos de dados. Foi utilizado para leitura e armazenamento dos arquivos CSV, manipulação dos dados de entrada e construção das saídas. Para instalação, execute o comando "pip install pandas"

## Arquivos de entrada

Os arquivos utilizados nesse projeto estão disponíveis na pasta Data deste repositório, e são constituídos de diversos arquivos CSV, contendo os dados de artigos, professores, áreas e departamentos da produção científica brasileira na área da ciência da computação. Os arquivos são definidos por um prefixo (Sendo este o nome da área de pesquisa) e por um sufixo (Que determina o conteúdo armazenado nele). A relação de sufixos por seu conteúdo é descrita abaixo:
* '-out-confs.csv': Conferências
* '-out-scores.csv': Scores de departamentos
* '-out-profs.csv': Professores
* '-out-papers.csv': Papers publicados

## Módulos

O projeto foi divido em módulos, para facilitar o entendimento do desenvolvedor, organizar melhor as funcionalidades e segregar constantes utilizadas no projeto: O conteúdo de cada um dos módulos é descrito a seguir: 
* Routes.py: Contém as rotas utilizadas pelo servidor, utilizadas quando ocorre uma requisição de um cliente. Utiliza para seu funcionamento diversas funções da biblioteca flask. Ao todo, são definidas quatro rotas, que serão descritas individualmente na seção “Rotas”. 
* Functions.py: Contém as funções responsáveis pelo funcionamento da API e as respectivas respostas entregues aos clientes. Utiliza funções da biblioteca flask e da biblioteca pandas. Cada função será descrita individualmente na seção “Funções” 
* Constants.py: Contém os valores constantes utilizados no projeto, que são os cabeçalhos dos arquivos CSV. 

## Funções

### Parâmetros de entrada

Em qualquer chamada, existem parâmetros obrigatórios e opcionais, que são descritos a seguir:
* areaName: Nome da área
* conferenceName: Nome da conferência
* departmentName: Nome do departamento
* teacherName: Nome do professor
* year: Ano de publicação

### Rotas

A API é constituída de quatro rotas, que segregam o conteúdo para os clientes e as funcionalidades da API. Cada rota possui parâmetros obrigatórios e opcionais, que definem o comportamento do programa e as funções corretas para serem executadas pelo servidor. Caso um parâmetro obrigatório não seja preenchido, o servidor retorna um erro para o cliente.  Cada uma das rotas é descrita a seguir:

* publicationsSection(): Rota para as funcionalidades referentes ao número de publicações. Possui um parâmetro obrigatório (areaName, que define o nome da área de interesse) e um parâmetro opcional (conferenceName, que define o nome da conferência). Caso somente o parâmetro obrigatório seja preenchido, o servidor redirecionará para a função que retorna o número de publicações no conjunto de conferências de uma área. Caso o parâmetro opcional também seja preenchido, o servidor redirecionará para a função que retorna o número de publicações em uma determinada conferência de uma área.
* scoreSection(): Rota para as funcionalidades referentes a scores de departamentos. Possui um parâmetro obrigatório (areaName, que define o nome da área de interesse) e um parâmetro opcional (departmenteName, que define o nome do departamento). Caso somente o parâmetro obrigatório seja preenchido, o servidor redirecionará para a função que retorna os scores de todos os departamentos em uma área. Caso o parâmetro opcional também seja preenchido, o servidor redirecionará para a função que retorna os scores de um determinado departamento em uma área.
* teachersSection(): Rota para as funcionalidades referentes ao número de professores. Possui um parâmetro obrigatório (areaName, que define o nome da área de interesse) e um parâmetro opcional (departmenteName, que define o nome do departamento). Caso somente o parâmetro obrigatório seja preenchido, o servidor redirecionará para a função que retorna o número de professores que publicam em uma determinada área (organizados por departamentos). Caso o parâmetro opcional também seja preenchido, o servidor redirecionará para a função que retorna o número de professores de um determinado departamento que publicam em uma área
* papersSection(): Rota para as funcionalidades referentes a lista de artigos. Necessita um parâmetro obrigatório (areaName, que define o nome da área de interesse, ou teachersName, que define o nome do professor) e dois parâmetros opcionais (departmenteName, que define o nome do departamento, ou year, que indica o ano da publicação). Caso somente o parâmetro “teacherName” seja preenchido, o servidor redirecionará para a função que retorna a lista de todos os papers de um determinado professor. Caso somente o parâmetro “areaName” seja preenchido, o servidor redirecionará para a função que retorna a lista de todos os papers de uma área (ano, título, deptos e autores). Caso esse parâmetro seja preenchido, e o parâmetro “Year” também, o servidor redirecionará para a função que retorna a lista de papers publicados em um determinado ano. Caso “areaName” seja preenchido e o parâmetro “departmentName” também, o servidor redirecionará para a função que retorna a lista de todos os papers de um departamento em uma área.

### Descrição das funções

* num_publications_by_conference_in_area(areaName, conferenceName): Número de publicações em uma determinada conferência de uma área
* num_publications_by_area(areaName): Número de publicações no conjunto de conferências de uma área
* department_scores(areaName): Scores de todos os departamentos em uma área
* department_score(areaName, departmentName): Score de um determinado departamento em uma área.
* num_teachers_by_area(areaName): Número de professores que publicam em uma determinada área (organizados por departamentos)
* num_teachers_in_department_by_area(areaName, departmentName): Número de professores de um determinado departamento que publicam em uma área
* papers_by_area(areaName): Todos os papers de uma área (ano, título, deptos e autores)
* papers_by_area_in_year(areaName, year): Todos os papers de uma área em um determinado ano
* papers_by_department_in_area(areaName, departmentName): Todos os papers de um departamento em uma área
* papers_by_teacher(teacherName): Todos os papers de um professor (dado o seu nome)

### Execução:

Para iniciar o servidor, digite o comando "python routes.py"
Para execução do cliente, existem dois procedimentos distintos:
* Para execução via browser: Ir ao endereço -http://localhost:5000/"rota?parametro1="valor do parametro">&parametro2="valor do parametro"...-
* Para execução via cliente: Executar via terminal - chmod +x APIclient.sh

## Retornos HTTP

* 200 : Arquivo CSV é retornado para o cliente com sucesso
* 404 : Arquivo de entrada nao foi encontrado
* 412: Parâmetros incorretos
* 422 : Resultado não encontrado