# 🎬 FLIX API - Sistema de Gerenciamento de Filmes

## 📖 Descrição

A **FLIX API** é uma API REST desenvolvida em Django durante meus estudos sobre o framework. Este projeto consiste em um sistema completo de gerenciamento de filmes, implementando funcionalidades de autenticação JWT, CRUD de filmes, gêneros, atores e avaliações. A API foi construída com foco no aprendizado de conceitos fundamentais do Django REST Framework.

## 🛠️ Tecnologias Utilizadas

- **Django** - Framework web em Python
- **Django REST Framework (DRF)** - Toolkit para construção de APIs REST
- **JWT (JSON Web Tokens)** - Sistema de autenticação e autorização segura
- **Python** - Linguagem de programação principal
- **SQLite** - Banco de dados relacional
- **PythonAnywhere** - Plataforma de hospedagem em nuvem

## ✨ Funcionalidades Principais

- 🔐 **Autenticação JWT** - Sistema seguro de login e autorização de usuários
- 🎥 **Gerenciamento de Filmes** - CRUD completo de filmes com informações detalhadas
- 🎭 **Controle de Gêneros** - Categorização de filmes por gêneros
- ⭐ **Sistema de Avaliações** - Avaliações e comentários sobre filmes
- 👥 **Gestão de Usuários** - Registro e autenticação de usuários
- 📊 **Serialização Avançada** - Conversão eficiente entre JSON e modelos Django
- 🛡️ **Validação Robusta** - Validações completas em todos os endpoints
- 📋 **Documentação Interativa** - Endpoints bem documentados

## 🌐 Links de Acesso

### 🚀 API em Produção
**[https://flixapilp.pythonanywhere.com/](https://flixapilp.pythonanywhere.com/)**

### 📚 Repositório GitHub
**[https://github.com/Leonardo-P-Monteiro/FLIX_API](https://github.com/Leonardo-P-Monteiro/FLIX_API)**

## 📚 Endpoints Disponíveis

### 👤 User e Password para obtenção do token.
```JSON
{
    "username": "user",
    "password": "user@12345"
}
```

### 🔑 Autenticação
```http
POST /api/v1/authentication/token/                       # Obter token JWT
POST /api/v1/authentication/verify/                      # Verificar o token JWT
POST /api/v1/authentication/token/refresh/               # Refresh do token JWT
```

### 🎬 Filmes
```http
GET    /api/v1/movies/                    # Listar todos os filmes
POST   /api/v1/movies/                    # Criar novo filme
GET    /api/v1/movies/{id}/               # Obter filme específico
PUT    /api/v1/movies/{id}/               # Atualizar filme completo
PATCH  /api/v1/movies/{id}/               # Atualização parcial de filme
DELETE /api/v1/movies/{id}/               # Deletar filme
GET    /api/v1/movies/stats/              # Estatísticas sobre o banco de dados
```

### 🎭 Gêneros
```http
GET    /api/v1/genres/                    # Listar todos os gêneros
POST   /api/v1/genres/                    # Criar novo gênero
GET    /api/v1/genres/{id}/               # Obter gênero específico
PUT    /api/v1/genres/{id}/               # Atualizar gênero
DELETE /api/v1/genres/{id}/               # Deletar gênero
```

### ⭐ Avaliações
```http
GET    /api/v1/reviews/                   # Listar todas as avaliações
POST   /api/v1/reviews/                   # Criar nova avaliação
GET    /api/v1/reviews/{id}/              # Obter avaliação específica
PUT    /api/v1/reviews/{id}/              # Atualizar avaliação
DELETE /api/v1/reviews/{id}/              # Deletar avaliação
```

### 👥 Atores
```http
GET    /api/v1/actors/                    # Listar todos os atores
POST   /api/v1/actors/                    # Criar novo ator
GET    /api/v1/actors/{id}/               # Obter ator específico
PUT    /api/v1/actors/{id}/               # Atualizar dados do ator
DELETE /api/v1/actors/{id}/               # Deletar ator
```

## 🧪 Como Testar a API

### 1. Usando cURL

#### Login e Obtenção de Token
```bash
curl -X POST https://flixapilp.pythonanywhere.com//api/v1/authentication/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "user",
    "password": "user@12345"
  }'
```

#### Listagem de Filmes (com autenticação)
```bash
curl -X GET https://flixapilp.pythonanywhere.com/api/v1/movies/ \
  -H "Authorization: Bearer SEU_TOKEN_JWT_AQUI"
```

#### Criação de Novo Filme
```bash
curl -X POST https://flixapilp.pythonanywhere.com/api/v1/movies/ \
  -H "Authorization: Bearer SEU_TOKEN_JWT_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Meu Filme Favorito",
    "genre": 1,
    "release_date": "2024-01-15",
    "actors": [1, 2],
    "resume": "Uma descrição interessante do filme"
  }'
```

### 2. Usando Python (requests)
```python
import requests

# URL base da API
BASE_URL = "https://flixapilp.pythonanywhere.com/api/v1"

# 1. Fazer login
login_data = {
    "username": "user",
    "password": "user@12345"
}

response = requests.post(f"{BASE_URL}/api/v1/authentication/token/", json=login_data)
token = response.json()['access']

# 2. Configurar headers com token
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# 3. Listar filmes
movies = requests.get(f"{BASE_URL}/movies/", headers=headers)
print(movies.json())

# 4. Criar novo filme
new_movie = {
    "title": "Novo Filme",
    "genre": 1,
    "release_date": "2024-12-01",
    "actors": [1],
    "resume": "Descrição do novo filme"
}

response = requests.post(f"{BASE_URL}/movies/", json=new_movie, headers=headers)
print(response.json())
```

### 3. Usando Postman

1. **Importe a Collection:**
   - Crie uma nova collection chamada "FLIX API"
   - Configure a Base URL: `https://flixapilp.pythonanywhere.com/api/v1`

2. **Configure Autenticação:**
   - Tipo: Bearer Token
   - Token: Obtido através do endpoint de login

3. **Teste os Endpoints:**
   - Comece com registro/login
   - Em seguida teste os endpoints de filmes, gêneros e avaliações

## 🏗️ Estrutura do Projeto

```
FLIX_API/
├── manage.py
├── requirements.txt
├── app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── authentication/     # App de autenticação
├── movies/             # App de filmes
├── genres/             # App de gêneros
├── actors/             # App de atores
├── reviews/            # App de avaliações
└── static/
```

## 💡 Habilidades Desenvolvidas

Durante o desenvolvimento deste projeto, foram consolidadas as seguintes competências técnicas:

### 🎯 Backend Development
- ✅ **Desenvolvimento de APIs REST** - Criação de endpoints robustos seguindo padrões REST
- ✅ **Django & Django REST Framework** - Domínio completo do framework e suas ferramentas
- ✅ **Autenticação e Autorização** - Implementação segura de JWT para controle de acesso
- ✅ **Modelagem de Banco de Dados** - Design de modelos relacionais complexos
- ✅ **Serialização Avançada** - Conversão eficiente entre formatos de dados

### 🔒 Segurança
- ✅ **JWT Authentication** - Implementação de autenticação stateless e segura
- ✅ **Validação de Dados** - Validações robustas em todos os inputs
- ✅ **Controle de Permissões** - Gestão granular de acesso aos recursos
- ✅ **CORS Configuration** - Configuração adequada para acesso cross-origin

### 🚀 DevOps & Deploy
- ✅ **Deploy em Produção** - Publicação da aplicação no PythonAnywhere
- ✅ **Gerenciamento de Dependências** - Controle eficiente com requirements.txt
- ✅ **Configuração de Ambiente** - Separação entre desenvolvimento e produção
- ✅ **Versionamento de API** - Estruturação para futuras versões

### 📊 Boas Práticas
- ✅ **Clean Code** - Código limpo e bem estruturado
- ✅ **Padrões REST** - Implementação correta de padrões RESTful
- ✅ **Documentação** - Documentação clara e completa da API
- ✅ **Tratamento de Erros** - Respostas consistentes e informativas

## 🎯 Importância do Projeto

Este projeto representa um marco no meu desenvolvimento como programador backend, demonstrando:

### 📈 **Crescimento Técnico**
- **Aplicação Prática**: Consolidação de conceitos teóricos em um projeto real e funcional
- **Complexidade Gerenciada**: Capacidade de lidar com múltiplos modelos e relacionamentos
- **Padrões Profissionais**: Adoção de metodologias e padrões utilizados na indústria

### 🔧 **Experiência Completa**
- **Full Cycle Development**: Desde o planejamento até o deploy em produção
- **Problem Solving**: Resolução de desafios reais de desenvolvimento
- **Production Ready**: API totalmente funcional e acessível online

### 🎓 **Aprendizado Consolidado**
- **Django Mastery**: Domínio avançado do framework Django
- **API Design**: Compreensão profunda de design de APIs REST
- **Security Implementation**: Implementação prática de segurança em aplicações web

## 🚀 Configuração para Desenvolvimento Local

```bash
# 1. Clone o repositório
git clone https://github.com/Leonardo-P-Monteiro/FLIX_API.git
cd FLIX_API

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute as migrações
python manage.py makemigrations
python manage.py migrate

# 5. Crie um superusuário (opcional)
python manage.py createsuperuser

# 6. Inicie o servidor de desenvolvimento
python manage.py runserver
```

A API estará disponível em: `http://localhost:8000/api/v1/`

---

**🎯 Status:** ✅ Funcional e hospedado no PythonAnywhere  
**📅 Período de Desenvolvimento:** Curso de Django (2025)  
**🔄 Última Atualização:** Setembro 2025  
**⭐ Versão Atual:** v1.0