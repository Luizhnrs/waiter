Waiter-django
Esta API, desenvolvida com Django, permite o gerenciamento de usuários, oferecendo funcionalidades de criação, leitura, atualização e exclusão de registros de usuários.

Endpoints
1. Listar Usuários
Endpoint: GET /api/users/

Descrição: Retorna uma lista de todos os usuários cadastrados.
Resposta:
Status: 200 OK
Exemplo de Corpo de Resposta:
json
Copiar código
[
  {
    "id": 1,
    "username": "usuario1",
    "email": "usuario1@email.com",
    "first_name": "Nome",
    "last_name": "Sobrenome"
  },
  {
    "id": 2,
    "username": "usuario2",
    "email": "usuario2@email.com",
    "first_name": "Nome2",
    "last_name": "Sobrenome2"
  }
]
2. Criar Usuário
Endpoint: POST /api/users/

Descrição: Cria um novo usuário.
Corpo da Requisição:
json
Copiar código
{
  "username": "novo_usuario",
  "email": "novo_usuario@email.com",
  "password": "senha_segura",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}
Resposta:
Status: 201 Created
Exemplo de Corpo de Resposta:
json
Copiar código
{
  "id": 3,
  "username": "novo_usuario",
  "email": "novo_usuario@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}
3. Obter Detalhes do Usuário
Endpoint: GET /api/users/{id}/

Descrição: Retorna os detalhes de um usuário específico.
Parâmetros de URL:
id: ID do usuário a ser consultado.
Resposta:
Status: 200 OK
Exemplo de Corpo de Resposta:
json
Copiar código
{
  "id": 1,
  "username": "usuario1",
  "email": "usuario1@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}
4. Atualizar Usuário
Endpoint: PUT /api/users/{id}/

Descrição: Atualiza os detalhes de um usuário específico.
Parâmetros de URL:
id: ID do usuário a ser atualizado.
Corpo da Requisição:
json
Copiar código
{
  "username": "usuario_atualizado",
  "email": "usuario_atualizado@email.com",
  "first_name": "NomeAtualizado",
  "last_name": "SobrenomeAtualizado"
}
Resposta:
Status: 200 OK
Exemplo de Corpo de Resposta:
json
Copiar código
{
  "id": 1,
  "username": "usuario_atualizado",
  "email": "usuario_atualizado@email.com",
  "first_name": "NomeAtualizado",
  "last_name": "SobrenomeAtualizado"
}
5. Deletar Usuário
Endpoint: DELETE /api/users/{id}/

Descrição: Remove um usuário do sistema.
Parâmetros de URL:
id: ID do usuário a ser removido.
Resposta:
Status: 204 No Content
Configuração do Projeto
Clone o repositório:
bash
Copiar código
git clone https://github.com/seu_usuario/seu_projeto.git
Instale as dependências:
bash
Copiar código
pip install -r requirements.txt
Aplique as migrações:
bash
Copiar código
python manage.py migrate
Inicie o servidor de desenvolvimento:
bash
Copiar código
python manage.py runserver
Autenticação
Essa API pode estar protegida por autenticação. Certifique-se de adicionar o cabeçalho de autenticação adequado (como um token JWT ou um token de sessão) nas requisições quando necessário.

Contribuição
Faça um fork do projeto
Crie uma branch para sua feature (git checkout -b feature/nome-da-feature)
Commit suas mudanças (git commit -m 'Adicionei uma nova feature')
Dê um push na branch (git push origin feature/nome-da-feature)
Abra um Pull Request
 
 
