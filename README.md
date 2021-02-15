# Debts API
This repository stores code from Zapay's Python Backend Developer coding challenge.

## Como rodar o projeto
1. O ideal é possuir um `virtualenv` para instalar as bibliotecas extras;
2. Instale as bibliotecas adicionais utilizadas ```pip3 install -r requirements.txt```
3. O projeto aceita 2 ou 3 argumentos para realizar a busca de débitos do carro.
   1. Resgatando todos os débitos disponíveis; ```$ python3 main.py ABC1234 11111111111```
   2. Resgatando débitos de um tipo em específico; ```$ python3 main.py ipva ABC1234 11111111111```
4. Rode os testes. ```pytest tests.py```
   
## Evoluções requiridas
1. Adicionar funcionalidade de resgatar todos os débitos.
A funcionalidade foi adicionada através de mudanças nos 3 principais arquivos. Sendo elas contempladas nos três commits "[Create mount debt data method](https://github.com/lucasdutraf/debts-api/commit/d1c9a7293702970f355bd1d4281e60087c0cbc4e)", "[Update main according to all debts return functionality](https://github.com/lucasdutraf/debts-api/commit/dd2c3f681b73fc5af7c8042156c793a18ba2e85c)", "[Create parsing function to return all debts](https://github.com/lucasdutraf/debts-api/commit/12384cf1b7bacfd4fe3f66b4e6f6a25cb51521e3)".  
2. Implementar um novo tipo de débito.
A funcionalidade foi adicionada através de mudanças nos 3 principais arquivos. Sendo elas contempladas nos três commits "[Create licensing debt option fetch logic](https://github.com/lucasdutraf/debts-api/commit/ff8a151c857472efa19d8663acb7ecb5e1718b85)", "[Add licensing debt option to parser](https://github.com/lucasdutraf/debts-api/commit/ee49e0ff25ca4eacad21e1e5a1be005461a2d300)", "[Update main logic to support licensing](https://github.com/lucasdutraf/debts-api/commit/79ae797508238124e11ea1d5d0bc76ba56a0a4ef)".  
3. Implementar uma solução que aceite placas de modelo novo como input.
A funcionalidade foi adicionada através de mudanças no arquivo `main.py`. Sendo ela contemplata em apenas um commits "[Add function for handling with new license plate pattern](https://github.com/lucasdutraf/debts-api/commit/d67a2f94cb97eebe3d1466d77023be3d25422963)".  
4. Adicionar testes na aplicação. Essa evolução foi atendida e foi utilizada a técnica de testes parametrizados, com o apoio da biblioteca `pytest`. Todos os testes implementados constam no arquivo `tests.py`.

Autor: Lucas Dutra Ferreira do Nascimento
