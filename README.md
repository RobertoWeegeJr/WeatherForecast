# WeatherForecast

A estrutura está dividida em três partes: database, backend e front end. 
Cada uma dessas partes é representada por uma pasta na raiz do projeto.

Database:
Foi utilizado MySQL 8.0.14.

Dentro da pasta database existem dois scripts que devem ser executados. São eles:
1- setup.sql
2- data-setup.sql
É necessário executar os dois, na sequencia apresentada, para realizar o setup da base de dados.

A base é composta por três tabelas. Uma que armazena os países, uma que armazena as cidades e uma que armazena as cidades cadastradas pelo usuário para visualização da previsão do tempo.
A modelagem foi feita dessa forma pois a API Open Weather recomenda a utilização do parâmetro id de cidade para solicitar os dados de previsão.Isto pois a utilização de outros parâmetros podem retornar dados ambíguos. Por isso foram armazenados na base os dados de países e cidades de acordo com as indicações da API.
Com isso também é possível fazer sugestão de valores para o imput do usuário, facilitando a utilização.

Backend
Foi utilizado Python 3.7.2.
Dependências:
- mysql
- json
- requests
- flask
- flask_restful
- flask_cors
- abc
- unittest

O backend é composto de cinco arquivos.
Os endpoints do serviço REST estão configurados em main.py. Esse é o arquivo que deve ser executado para rodar o server.
O arquivo database.py é responsavel por realizar a comunicação com a base de dados. É nesse aquivo, e somente nele, que os statements sql foram declarados. Neste arquivo os dados da base são transformados em dados da modelagem e vice-versa.
O arquivo forecast.py tem uma função similar à função do database.py. Ele é o único que realiza comunicação com a API Open Weather. Assim que obtem os dados eles são submetidos à modelagem criada para a aplicação.
O arquivo model.py contem a declaração de todas as classes que representam os objetos utilizados pelo backend.
O arquivo test_unity.py contem os testes unitarios criados para validar as interações com o banco de dados.
As configurações de apontamento para a base MySQL estão no arquivo database_connection.json

Frontend
Foi utilizado Angular 7.2.
As dependências estão descritas no arquivo package.json. Portanto basta ter o Node.js instalado e executar o comando "npm install" na pasta frontend/CitiesForecast. Com isso o ambiente irá ser configurado. Após a configuração o comando "ng serve" deve iniciar o servidor web.

O frontend está dividido em quatro partes.
A primeira representa a tela inicial do sistema. Nela são exibidos os campos para cadastro das cidades e a lista de cidades já cadastradas (classe AppComponent).
A segunda parte representa o dialog que é criado para exibir os dados de previsão do tempo (classe ForecastComponent).
A terceira parte é responsável por realizar a comunicação com o backend, realizando as chamadas REST e populando os objetos de modelo para disponibilizar para os dois componentes anteriores (classe DataService).
A última parte é responsavel por declarar a representação dos dados utilizados no frontend (arquivo model.ts). 
O apontamento para o server de backend é realizado no arquivo frontend/CitiesForecast/scr/environments/environment.ts.
