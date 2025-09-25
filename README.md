# 🎶API Instrumentos

<div align="center">
  <img height="180em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>

## Sumário 🔄

1. [Descrição](#descrição-)
2. [Tecnologias](#tecnologias)
3. [Desenvolvimento](#desenvolvimento-)
4. [Configuração do Ambiente](#-configuração-do-ambiente)
5. [Modo de Uso](#modo-de-uso-)
6. [Testes Automatizados](#testes-automatizados-)
7. [Autenticação JWT](#-autenticação-jwt-no-fastapi)
8. [ORM SQLAlchemy](#️orm-sqlalchemy)

---
## Descrição 📝
Esta é uma API desenvolvida em Python com o framework FastAPI, estruturada seguindo o padrão de arquitetura MVC (Model-View-Controller). A aplicação utiliza PostgreSQL como banco de dados com ORM SQLAlchemy.

Para garantir segurança nas requisições, a API implementa autenticação via JWT (JSON Web Token), assegurando que apenas usuários autorizados possam acessar os recursos disponíveis.

Além disso, a aplicação conta com testes automatizados, garantindo a qualidade, integridade e confiabilidade das funcionalidades implementadas.

## Tecnologias
<div align="left">
    <img src="https://skillicons.dev/icons?i=py" height="40" alt="python logo"/>
    <img src="https://skillicons.dev/icons?i=fastapi" height="40" alt="fastapi logo"/>
    <img src="https://skillicons.dev/icons?i=postgres" height="40" alt="postgresql logo"/>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNYous45csrFJY35QaDwGHGoijcFjR57FjAs4tiQ-BiLVJF2HeEt06zDT-KuHsXU9L&usqp=CAU" height="40" alt="pytest logo"/>
    <img src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/pytestlogo.jpg" height="40" alt="pytest logo"/>
    <img src="data:image/png;base64,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"height="40" alt="jwt logo">
</div>

## Desenvolvimento 👨‍💻
`Controller` ✅
- Gerenciar as requisições `HTTP`
-  🟢**GET**
-  🔵**POST**
-  🟠**PATCH**
-  🔴**DELETE**

`Models` ✅
- Define as estruturas dos dados e suas interações com o banco de dados.

`Schema` ✅
- Validado via Pydantic:
  - Validar dados de entrada (request body).
  - Definir o formato dos dados de saída (response model).
  - Documneta automaticamente no Swagger

`Repository` ✅
- Abstrai o acesso aos dados, fornecendo uma interface para interagir com o banco de dados sem expor sua implementação, facilitando o teste e a manutenção do código.

`Service` ✅
-  Orquestrar as operações, utilizando os Repositories e outras dependências para realizar ações específicas, como validações e transformações de dados.

`Test` ✅ 
Testes automatizados para verificar o comportamento das camadas de Service, Repository, e outras partes do sistema, garantindo que as funcionalidades estejam corretas e que futuras mudanças não quebrem o sistema.

`Autenticação JWT` ✅
JWT (JSON Web Token) é um padrão aberto para autenticação e troca segura de informações entre duas partes, usando um token compacto e autossuficiente.
- Ao fazer login ou uma requisição autenticada, o servidor gera um token JWT, que contém dados do usuário e uma data de expiração.
- Esse token é assinado com uma chave secreta para garantir sua integridade.
- O cliente (ex: frontend ou outro sistema) envia esse token no header da requisição
- O servidor valida o token em cada requisição:
  - Se for válido e não estiver expirado → libera o acesso
  - Se inválido ou expirado → bloqueia a requisição

### Diretório 🗂️
```plaintext
📦 Kevin Soffa | Instrumentos API
 ┣ 📂 auth
 ┣ 📂 controller
 ┣ 📂 core
 ┣ 📂 migrations
 ┣ 📂 models
 ┣ 📂 repository
 ┣ 📂 schema
 ┣ 📂 service
 ┣ 📂 test 
 ┣ 📜 .env
 ┣ 📜 .gitignore
 ┣ 📜 main.py
 ┣ 📜 alembic.ini
 ┗ 📜 requirements.txt
```

### 🔧 Configuração do Ambiente 
#### Instalando bibliotecas necessárias
- 💻 Crie um ambiente virtual
```bash
python -m venv {nome-da-sua-venv}
```

- ▶️ Ative o ambiente virtual
```bash
{nome-da-sua-venv}\Scripts\activate
```

- 🏗️ Instalar todas as bibliotecas nessárias
```bash
pip install -r requirements
```

Antes de executar o projeto, configure as seguintes variáveis de ambiente no seu arquivo `.env` ou diretamente no sistema (toda conexão de banco de dados é feita aqui):

| Variável              | Descrição                                           | tipo        |
|-----------------------|-----------------------------------------------------|-------------|
| HOST                  | Define o endereço do servidor do banco de dados     |  str        |
| DATABASE              | Nome do banco de dados que a aplicação irá utiliza  |  str        |
| USER                  | Nome de usuário para autenticação no banco de dados |  str        |
| PASSWORD              | Senha do usuário para acessar o banco de dados      |  str        |
| SECRET_KEY            | Chave secreta para geração de Token [ JWT ]         |  str        |
| ALGORITHM             | Algoritmo de criptografia o JWT vai usar            |  str        |
| USER_NAME_LOGIN       | Usuário para Login para criação de Token            |  str        |
| PASSWORD_LOGIN        | Senha do usário para criação de Token               |  str        |



### 📂 Exemplo de arquivo `.env`
```plaintext
##################################################
### CONEXÃO BANCO DE DADOS
##################################################
HOST=
DATABASE=
PASSWORD=
USER=

##################################################
### JWT
##################################################
SECRET_KEY=
ALGORITHM=

USER_NAME_LOGIN=
PASSWORD_LOGIN=
```

#### ⚡ Para iniciar o servidor local python via prompt de comando basta rodar o comando a baixo na pasta raiz
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### ⚡Para acessar o Swagger
```bash
localhost/docs
```
#### 📚SWAGGER
<img src="https://raw.githubusercontent.com/KevinSoffa/API-Instrumentos-SQLAlchemy/refs/heads/master/img/swagger.png" height="500" alt="criação de tabelas no banco de dados"/>
--

## Modo de Uso 🔄
### Consulta ALL
GET🟢
 ```bash
/instruments/
```
RESPOSTA ⬇️
 ```bash
HTTP 200 OK
[
  {
    "nome": "string",
    "marca": "string",
    "preco": 0,
    "modelo": "string",
    "orquestra": true,
    "comentario": "string",
    "id": 0
  }
]
```
***
### Criar Produto
POST 🔵
 ```bash
/instruments/
```
JSON EXEMPLO ⬆️
 ```bash
{
  "nome": "string",
  "marca": "string",
  "preco": 0,
  "modelo": "string",
  "orquestra": true,
  "comentario": "string"
}
```
RESPOSTA ⬇️
```bash
HTTP 201
{
  "nome": "Trompete",
  "marca": "YAMAHA",
  "preco": 12500,
  "modelo": "XENON - New York",
  "orquestra": true,
  "comentario": "Instrumento de Metal",
  "id": 4
}
```
***
### Consultar Instrumentos
GET🟢
 ```bash
/instruments/{/instruments_id}
```
RESPOSTA ⬇️
```bash
HTTP 200 OK
 {
   "nome": "string",
   "marca": "string",
   "preco": 0,
   "modelo": "string",
   "orquestra": true,
   "comentario": "string",
   "id": 0
 }
```
***
### Atualizar Cliente
PATCH🟠
 ```bash
/instruments/{/instruments_id}
```
JSON
```bash
 {
   "nome": "string",
   "marca": "string",
   "preco": 0,
   "modelo": "string",
   "orquestra": true,
   "comentario": "string",
   "id": 0
 }
```
RESPOSTA ⬇️
```bash
HTTP 200
 {
   "nome": "string",
   "marca": "string",
   "preco": 0,
   "modelo": "string",
   "orquestra": true,
   "comentario": "string",
   "id": 0
 }
```
### Apagar Cliente
DELETE🔴
 ```bash
/instruments/{/instruments_id}
```
RESPOSTA ⬇️
```bash
HTTP 204
```

## Testes Automatizados 🧪
### teste [ Services ] ⏩
 ```bash
{diretorio}/{script}/tests/service pytest -v
```
<img src="https://raw.githubusercontent.com/KevinSoffa/API-Instrumentos-SQLAlchemy/refs/heads/master/img/pytest.png" height="200" alt="teste automatizados"/>

## 🔐 Autenticação JWT no FastAPI
#### Instrumentos API utiliza autenticação via JWT (JSON Web Token) para proteger rotas da API.

### 📌 Como funciona:
#### 1 Geração de Token

 - Após login, a API gera um token JWT.
 - O token é assinado com uma chave secreta (SECRET_KEY).
#### Exemplo de Login para gerar o TOKEN
#### POST 🔵
 ```bash
/kevinsoffa/login
```
#### JSON de envio ⬆️
 ```bash
{
    "usuário":"user",
    "senha":"password"
}
```
#### Resposta ⬇️ 
```bash
HTTP 200 OK
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrZXZpbl9zb2ZmYSIsImV4cCI6MTc1MTMzOTQxNX0.bKYqFWqpSrw4lA-MI-YRdC-_x7M4nNrwi7WYFCm2hPY"
}
```

#### 2 Envio do Token
- O cliente (frontend ou API client) deve enviar o token no header da requisição:
```bash
Authorization: Bearer <token>
```

#### 3 Validação do Token
- As rotas protegidas usam a dependência de segurança JWTBearer.
- Ao receber a requisição, a API:
  - Extrai o token do header
  - Valida assinatura e expiração (30min)
  - Se inválido ou expirado → retorna erro 403 Forbidden
  - Se válido → libera o acesso à rota

#### 📄 Configuração:
As variáveis de autenticação devem estar no arquivo .env

## 🗄️ORM SQLAlchemy
### ✅Criação de Tabelas no Banco de dados
<img src="https://raw.githubusercontent.com/KevinSoffa/API-Instrumentos-SQLAlchemy/refs/heads/master/img/orm_create_table.png" height="400" alt="criação de tabelas no banco de dados"/>

### ✅Migrations [ alembic ]
<img src="https://raw.githubusercontent.com/KevinSoffa/API-Instrumentos-SQLAlchemy/refs/heads/master/img/orm_migrations.png" height="200" alt="Migração das tabelas"/>