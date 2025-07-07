# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

Projeto acadêmico desenvolvido para a disciplina de Projeto Multidisciplinar. O SGHSS tem como objetivo centralizar e organizar os processos hospitalares e clínicos em uma única aplicação web baseada em APIs RESTful.

## 🏥 Visão Geral

O sistema contempla a gestão de:
- Pacientes
- Profissionais de saúde
- Consultas
- Prontuários
- Receitas digitais
- Leitos hospitalares
- Suprimentos
- Logs de auditoria
- Autenticação e autorização via JWT

---

## 📌 Funcionalidades

- Cadastro e gerenciamento de usuários com diferentes perfis (`admin`, `paciente`, `profissional`)
- Agendamento de consultas
- Registro de prontuários médicos
- Emissão de receitas digitais
- Controle de ocupação de leitos
- Gestão de estoque de suprimentos
- Geração de logs e rastreamento de ações
- API segura com autenticação JWT

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.13+**
- **Django 5.2.2**
- **Django REST Framework**
- **Simple JWT (Token JWT)**
- **SQLite3** (banco padrão, mas adaptável para PostgreSQL)
- **Postman** (para testes de API)

---

## 🧭 Como Executar o Projeto Localmente

### 1. Clone o repositório:
```bash
git clone https://github.com/FelipeRn7/SGHSS.git
cd SGHSS

Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate  # Windows

Instale as dependências
pip install django djangorestframework djangorestframework-simplejwt

Execute as migrações:
python manage.py makemigrations
python manage.py migrate

Rode o servidor:
python manage.py runserver

🔐 Autenticação
O sistema utiliza autenticação via JWT.
Endpoints disponíveis:
POST /api/login/ → login com username e password
POST /api/login/refresh/ → renovar token
Use o token obtido para autenticação Bearer nos demais endpoints protegidos.

🧪 Testes
Os testes foram realizados com o Postman, simulando os seguintes fluxos:
Registro de usuários
Geração de token
Criação e recuperação de entidades (CRUD)
Acesso controlado por tipo de usuário

📂 Organização dos Aplicativos
App	Responsabilidade
usuarios	Registro, autenticação e tipos de usuários
pacientes	Cadastro de pacientes e seus dados
profissionais	Cadastro de profissionais de saúde
consultas	Agendamento e controle de consultas
prontuarios	Registro de prontuários clínicos
receitas	Emissão de receitas médicas
leitos	Gestão de leitos hospitalares
suprimentos	Controle de estoque hospitalar
logs	Auditoria e rastreamento de ações

📄 Licença
Projeto acadêmico sem fins lucrativos. Código aberto para fins didáticos.



