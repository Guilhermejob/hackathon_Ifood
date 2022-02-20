#### Primeira versão 

# House Chef V1

## Documentação

#


### O problema a ser solucionado

Sempre foi muito desagradável ir ao mercado e depois perceber que um ou mais items da sua lista não se encontra lá, alem de tomar tempo, temos que nos deslocar novamente em busca do item. Da mesma forma que por aplicativos, ficar procurando item por item da receita pode se tornar uma tarefa tediosa, o ideal mesmo seria uma aplicação onde você pesquisa uma receita e com base nos ingredientes dela é feita uma busca nos mercados proximos dando prioridade para o mercado que contém todos os item da lista, sem precisar ficar buscando item por item e melhor de tudo, com um unico toque obter todos os ingredientes em um mesmo mercado perto de sua casa

### A Solução

A magia esta no server side da aplicação, onde a partir de uma receita que o usuário procurar, tendo a sua lista de ingredientes como fonte de pesquisa, a aplicação irá vasculhar o banco de dados procurando mercados que estejam próximos ao cliente e que contenham os produtos referentes a receita pesquisada, dando preferência aos mercados que ofereçam mais vantagens ao usuário (distância, preço, frete, etc...).

#

## Instalação

- Primeiro faça o fork deste [repositório](https://github.com/Guilhermejob/hackathon_Ifood).

- Em seguida faça um git clone para a sua maquina

- Crie o ambiente um ambiente [virtual em python](https://docs.python.org/pt-br/3/tutorial/venv.html)

```
$ python -m venv venv --upgrade-deps
```

- Entre no ambiente virtual

```
$ source venv/bin/activate
```

- Instale as dependencias no arquivo `requirements.txt`

```
$ pip install -r requirements.txt
```

- Configure suas variáveis segundo o arquivo `.env.example`

  - Não esqueça de criar o seu banco de dados e adicionar no .env

- Crie as tabelas no banco de dados através do comando

```
$ flask db upgrade
```

- Inicie a aplicação local através do comando

```
$ flask run
```

- A aplicação inicializará na rota http://127.0.0.1:5000/. Você deverá ver algo semelhante ao snippet logo abaixo no seu terminal:

```
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 112-925-941
```

#

## Tecnologias usadas
 - Python
 - Flask
 - SQALAlchemy
 - Postgresql
 - ORM

## Documentação das rotas e retornos

### Registrando Super mercado
#### POST /supermarkets

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/154846098-65e4e4c8-10f2-4f30-8438-8453c382be90.png" width="700px" />
</div>


#

### Listando mercado por id
#### GET /supermarkets/<id:int>


<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/154846233-599f0347-c8ab-41cb-8812-69bcecbe474e.png" width="700px" />
</div>


> #### OBS : O "id" na rota é referente ao id do supermercado que deseja procurar, caso você passe um id que não exista, ele irá dar erro

#

### Registrando produto
#### POST /products

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/154846458-ad0447a8-6083-486d-a716-18ec0cdc9919.png" width="700px" />
</div>

> #### OBS : O "super_market_id" é referente ao id do supermercado que deseja cadastrar o produto, caso você passe um id que não exista, ele irá dar erro

#

### Listando produtos por nome  
#### GET /products/<name:str>

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/154846736-2a1f9fab-b5cb-423a-973d-b3da932cea87.png" width="700px" />
</div>

#

### Listando produtos da receita
#### GET /recipe/<id:int>/products

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/154846878-add35f89-fa88-42d1-a454-8c8a1b7297de.png" width="700px" />
</div>

> #### OBS : O id na rota é referente ao id da receita que deseja procurar, caso você passe um id que não exista, ele irá dar erro

#

### Registrando receita
#### POST /recipe

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/154847063-98998bb1-6dd7-4416-ad3d-fce1572c35c4.png" width="700px" />
</div>

#

### Listanto receita por nome
#### POST /recipe/<name:str>

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/154847164-b676ec63-0e7d-44b5-ac1d-3e907e4e6afb.png" width="700px" />
</div>

#

### Registrando ingredientes na receita
#### POST /ingredient/list

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/154847297-9a7cb58c-11f6-4f64-be3c-60ad80640508.png" width="700px" />
</div>

> #### OBS : Atenção, a chave "recipe" é obrigatória e deve receber o nome da receita que os ingredientes pertencem

#

## Desenvolvedores

### Está aplicação back end foi desenvolvida entre os dias 18/02/2022 até o dia 20/02/2022

- [Guilherme Job](https://www.linkedin.com/in/guilherme-armesto-job/)
- [Miqueias Carvalho](https://www.linkedin.com/in/miqueias-carvalho-dos-santos/)







