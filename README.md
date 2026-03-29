<<<<<<< HEAD
# 🐕 Carteira Digital Pet

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://djangoproject.com/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-red.svg)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3+-purple.svg)](https://getbootstrap.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Sistema web para gerenciamento digital de carteiras de vacinação de pets**

---

## 📋 Sobre o Projeto

O **Carteira Digital Pet** é um sistema web desenvolvido como parte do **Projeto Integrador em Computação I (PJI110)** da **UNIVESP**, aplicando a metodologia **Design Thinking** para resolver o problema real de perda e esquecimento de carteiras de vacinação físicas.

### 🎯 Problema Identificado
- Tutores de pets frequentemente perdem carteiras físicas de vacinação
- Esquecimento de datas para próximas doses
- Dificuldade de organizar histórico médico completo
- Falta de lembretes automáticos para revacinação

### 💡 Nossa Solução
Sistema web que permite:
- ✅ Cadastro e gerenciamento de múltiplos pets
- ✅ Registro completo de histórico de vacinação
- ✅ Lembretes automáticos para próximas doses
- ✅ Acesso online de qualquer dispositivo
- ✅ Interface intuitiva e responsiva
- ✅ Controle de veterinários e clínicas

---

## 🏗️ Arquiteturas Disponíveis

Este projeto oferece **duas implementações** para atender diferentes preferências de desenvolvimento:

### 🥇 **Opção 1: Django (Principal)**
```
django_app/
├── carteira_pet/          # Configurações do projeto
├── apps/
│   ├── core/             # Usuários, tutores, veterinários
│   ├── pets/             # Gerenciamento de pets
│   └── vacinas/          # Sistema de vacinação
├── templates/            # Templates HTML
└── static/              # Arquivos estáticos
```

### 🥈 **Opção 2: Flask (Alternativa)**
```
src/
├── app/
│   ├── models/          # SQLAlchemy models
│   ├── routes/          # Flask blueprints
│   ├── templates/       # Jinja2 templates
│   └── static/          # CSS, JS, imagens
├── config.py            # Configurações Flask
└── run.py              # Script de execução
```

---

## 🗄️ Modelo de Dados

Baseado no esquema SQL fornecido, com as seguintes entidades principais:

```
📊 DIAGRAMA CONCEITUAL:

Usuario (1) ──────► (1) Tutor (1) ──────► (N) Pet
                                             │
                                             │ (N)
                                             ▼
                                          Vacina ◄──── (N) Veterinario
                                             │              ▲
                                             └──────────────┘
                                                   (N:M)
```

### 🔍 Principais Tabelas:
- **`usuario`**: Sistema de login e autenticação
- **`tutor`**: Dados pessoais e endereço dos tutores
- **`especie`**: Canina, Felina, Ave, etc.
- **`pet`**: Informações completas dos pets
- **`veterinario`**: Dados dos profissionais
- **`vacina`**: Histórico completo de vacinação
- **`pet_veterinario`**: Relacionamento many-to-many

---

## 🚀 Instalação e Configuração

### 📋 Pré-requisitos
- **Python 3.8+**
- **Git** (para controle de versão)
- **MySQL 8.0+** (ou SQLite para desenvolvimento)
- **Node.js** (opcional, para ferramentas de build)

### 🔧 Configuração Inicial

1. **Clone o repositório:**
```bash
git clone https://github.com/equipe/carteira-pet-digital.git
cd carteira-pet-digital
```

2. **Crie um ambiente virtual:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

### 🐍 Opção Django (Recomendada)

3. **Instale as dependências:**
```bash
pip install -r requirements-django.txt
```

4. **Configure o banco de dados:**
```bash
# Crie um arquivo .env na raiz:
# DB_NAME=carteira_pet
# DB_USER=root
# DB_PASSWORD=sua_senha
# DB_HOST=localhost
# DB_PORT=3306
# SECRET_KEY=sua-chave-secreta-aqui

# Para usar SQLite durante desenvolvimento:
# USE_SQLITE=True
```

5. **Execute as migrações:**
```bash
cd django_app
python manage.py makemigrations
python manage.py migrate
```

6. **Crie um superusuário:**
```bash
python manage.py createsuperuser
```

7. **Execute o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

### 🌶️ Opção Flask (Alternativa)

3. **Instale as dependências Flask:**
=======
# Web Crawler da Univesp 🕷️

Este projeto implementa um web crawler básico que visita sistematicamente as páginas Web da Univesp, seguindo hyperlinks da página principal e contabilizando a frequência de cada palavra encontrada nas páginas visitadas.

## 📋 Funcionalidades

- ✅ Crawling sistemático do site da Univesp
- ✅ Seguimento de hyperlinks internos
- ✅ Extração e limpeza de texto HTML
- ✅ Contagem de frequência de palavras
- ✅ Filtro de stopwords em português
- ✅ Relatórios detalhados de análise
- ✅ Salvamento de resultados em arquivo
- ✅ Interface com progresso em tempo real

## 📁 Arquivos

### Versões Disponíveis:

1. **`univesp_crawler.py`** - Versão completa com bibliotecas externas (requests, BeautifulSoup)
2. **`univesp_crawler_simple.py`** - Versão simplificada usando apenas bibliotecas padrão do Python
3. **`Desafio_Semana_4.ipynb`** - Notebook Jupyter original com código base

### Arquivos Auxiliares:

- **`requirements.txt`** - Dependências para a versão completa
- **`README.md`** - Este arquivo com instruções

## 🚀 Como Executar

### Opção 1: Versão Simplificada (Recomendada)

Esta versão usa apenas bibliotecas padrão do Python, não requer instalação de dependências:

```bash
python univesp_crawler_simple.py
```

### Opção 2: Versão Completa

1. Instale as dependências:
>>>>>>> 6f1f496a79ffdabebdc5a166163226430658929f
```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
4. **Configure o ambiente:**
```bash
# Crie um arquivo .env:
# SECRET_KEY=sua-chave-secreta-aqui
# DATABASE_URL=mysql://user:password@localhost/carteira_pet
# FLASK_ENV=development
```

5. **Execute o servidor:**
```bash
python run.py --debug
```

Acesse: http://127.0.0.1:5000

---

## 🛠️ Stack Tecnológico

### **Backend**
- **Python 3.8+** - Linguagem principal
- **Django 4.2+** / **Flask 3.0+** - Frameworks web
- **MySQL 8.0+** - Banco de dados principal
- **SQLite** - Banco para desenvolvimento
- **SQLAlchemy** / **Django ORM** - Mapeamento objeto-relacional

### **Frontend**
- **HTML5 + CSS3** - Estrutura e estilização
- **Bootstrap 5.3** - Framework CSS responsivo
- **JavaScript ES6+** - Interatividade
- **Font Awesome** - Ícones
- **Jinja2** / **Django Templates** - Sistema de templates

### **Ferramentas de Desenvolvimento**
- **Git + GitHub** - Controle de versão
- **VS Code** - Editor recomendado
- **Python Decouple** - Configuração por variáveis de ambiente
- **Pytest** - Framework de testes
- **Black** + **Flake8** - Formatação e lint

### **Deploy e Produção**
- **Gunicorn** - Servidor WSGI
- **WhiteNoise** - Servir arquivos estáticos
- **MySQL** / **PostgreSQL** - Bancos para produção

---

## 📁 Estrutura do Projeto

```
carteira-pet-digital/
├── 📁 docs/                     # Documentação do projeto
│   ├── requisitos/              # Análise de requisitos
│   ├── wireframes/              # Protótipos de tela
│   ├── diagramas/               # Diagrama ER, arquitetura
│   ├── referencias/             # Bibliografia ABNT
│   └── design_thinking/         # Artefatos do DT
│
├── 📁 django_app/               # 🥇 IMPLEMENTAÇÃO DJANGO
│   ├── carteira_pet/            # Configurações principais
│   │   ├── settings.py          # Configurações Django
│   │   ├── urls.py              # URLs principais
│   │   └── wsgi.py              # Interface WSGI
│   ├── apps/
│   │   ├── core/                # App de usuários/tutores
│   │   ├── pets/                # App de pets
│   │   └── vacinas/             # App de vacinação
│   ├── templates/               # Templates HTML
│   ├── static/                  # CSS, JS, imagens
│   └── manage.py               # Comando Django
│
├── 📁 src/                      # 🥈 IMPLEMENTAÇÃO FLASK
│   ├── app/
│   │   ├── models/              # Modelos SQLAlchemy
│   │   ├── routes/              # Blueprints Flask
│   │   ├── templates/           # Templates Jinja2
│   │   └── static/              # Arquivos estáticos
│   └── __init__.py
│
├── 📁 tests/                    # Testes automatizados
│   ├── test_models.py
│   ├── test_views.py
│   └── test_integration.py
│
├── 📄 requirements-django.txt   # Dependências Django
├── 📄 requirements.txt          # Dependências Flask
├── 📄 config.py                 # Configurações Flask
├── 📄 run.py                    # Script execução Flask
├── 📄 .gitignore               # Arquivos ignorados
├── 📄 README.md                # Este arquivo
├── 📄 CONTRIBUTING.md          # Guia de contribuição
└── 📄 LICENSE                  # Licença MIT
```

---

## 👥 Equipe de Desenvolvimento

| Integrante | Papel | Responsabilidades | GitHub |
|------------|-------|------------------|---------|
| **Integrante 1** | 🎯 **Líder / Product Owner** | Coordenação, prazos, comunicação | [@usuario1](https://github.com/usuario1) |
| **Integrante 2** | 🏗️ **Arquiteto / Tech Lead** | Arquitetura, tecnologias, code review | [@usuario2](https://github.com/usuario2) |
| **Integrante 3** | ⚙️ **Desenvolvedor Backend** | APIs, lógica de negócio, rotas | [@usuario3](https://github.com/usuario3) |
| **Integrante 4** | 🗄️ **Especialista BD** | Modelos, migrations, otimização | [@usuario4](https://github.com/usuario4) |
| **Integrante 5** | 🎨 **Desenvolvedor Frontend/UX** | Interface, design, responsividade | [@usuario5](https://github.com/usuario5) |
| **Integrante 6** | 👥 **UX Researcher** | Entrevistas, personas, validação | [@usuario6](https://github.com/usuario6) |
| **Integrante 7** | 📚 **Documentador / QA** | Documentação, testes, qualidade | [@usuario7](https://github.com/usuario7) |

---

## 🔄 Metodologia: Design Thinking

Este projeto segue rigorosamente a metodologia **Design Thinking** em 5 fases:

### 1️⃣ **EMPATIA** (Quinzenas 1-2) ✅
- **7-10 entrevistas** com tutores de pets
- **Mapa de empatia** consolidado
- **2-3 personas** detalhadas
- **Insights** documentados

### 2️⃣ **DEFINIÇÃO** (Quinzenas 3-4)
- Síntese dos problemas identificados
- **Point of View** definido
- **Como podemos...** formulado

### 3️⃣ **IDEAÇÃO** (Quinzenas 5-6)
- Brainstorming de soluções
- Priorização de funcionalidades
- **MVP** definido

### 4️⃣ **PROTOTIPAÇÃO** (Quinzenas 7-11)
- Desenvolvimento do sistema
- **Testes internos** contínuos
- **Iterações** baseadas em feedback

### 5️⃣ **TESTE** (Quinzenas 12-14)
- **Validação com usuários** reais
- Coleta de feedback
- **Refinamentos finais**
- Documentação dos aprendizados

---

## 🚀 Como Executar

### 🖥️ Desenvolvimento Local

**Django:**
```bash
cd django_app
python manage.py runserver --settings=carteira_pet.settings
```

**Flask:**
```bash
python run.py --debug --port=5000
```

### 🧪 Executar Testes

**Django:**
```bash
cd django_app
python manage.py test
```

**Flask:**
```bash
pytest tests/ -v
```

### 🚀 Deploy em Produção

1. **Configure variáveis de ambiente:**
```bash
export SECRET_KEY="sua-chave-super-secreta"
export DB_HOST="servidor-mysql"
export DB_PASSWORD="senha-segura"
export DEBUG=False
```

2. **Execute com Gunicorn:**
```bash
# Django
gunicorn django_app.carteira_pet.wsgi:application

# Flask  
gunicorn "src.app:create_app()"
```

---

## 📊 Funcionalidades Principais

### 🎯 **Core Features (MVP)**
- [x] **Sistema de login** e cadastro de usuários
- [x] **Cadastro de tutores** com endereço completo
- [x] **Gerenciamento de pets** (nome, espécie, raça, idade)
- [x] **Registro de vacinas** com data e veterinário
- [x] **Visualização de histórico** de vacinação
- [x] **Interface responsiva** para mobile

### 🚀 **Features Avançadas (Quinzenas 9-10)**
- [ ] **Lembretes automáticos** via email/SMS
- [ ] **Calendário** de próximas vacinação
- [ ] **Dashboard analytics** para tutores
- [ ] **Relatórios PDF** da carteira
- [ ] **Upload de fotos** dos pets
- [ ] **Geolocalização** de veterinários próximos
- [ ] **API REST** para integração mobile

### 🎨 **Melhorias UX/UI**
- [ ] **Dark mode** toggle
- [ ] **PWA** (Progressive Web App)
- [ ] **Offline sync** básico
- [ ] **Multi-idioma** (português/inglês)

---

## 🔧 Configuração de Desenvolvimento

### 📝 **Variables de Ambiente**

Crie um arquivo `.env` na raiz do projeto:

```env
# === CONFIGURAÇÕES GERAIS ===
SECRET_KEY=django-insecure-mude-em-producao-123456789
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# === BANCO DE DADOS ===
# Para MySQL:
DB_NAME=carteira_pet
DB_USER=root
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306

# Para SQLite (desenvolvimento):
USE_SQLITE=True

# === EMAIL (desenvolvimento) ===
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# === UPLOADS ===
MEDIA_ROOT=media/
STATIC_ROOT=staticfiles/
```

### 🗃️ **Configuração do MySQL**

```sql
-- Criar banco de dados
CREATE DATABASE carteira_pet CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Criar usuário (opcional)
CREATE USER 'carteira_user'@'localhost' IDENTIFIED BY 'senha_segura';
GRANT ALL PRIVILEGES ON carteira_pet.* TO 'carteira_user'@'localhost';
FLUSH PRIVILEGES;
```

### 🏃‍♂️ **Scripts de Desenvolvimento**

**Django - Comandos úteis:**
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações  
python manage.py migrate

# Criar dados de teste
python manage.py loaddata fixtures/initial_data.json

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell interativo
python manage.py shell
```

**Flask - Comandos úteis:**
```bash
# Executar com debug
python run.py --debug

# Executar testes
python -m pytest

# Executar com auto-reload
python run.py --debug --host=0.0.0.0
```

---

## 📱 API REST (Futura)

### 🔍 **Endpoints Planejados**

```bash
# Autenticação
POST /api/auth/login/
POST /api/auth/logout/
POST /api/auth/register/

# Pets
GET  /api/pets/               # Listar pets do usuário
POST /api/pets/               # Criar novo pet
GET  /api/pets/{id}/          # Detalhes de um pet
PUT  /api/pets/{id}/          # Atualizar pet
DEL  /api/pets/{id}/          # Excluir pet

# Vacinas
GET  /api/pets/{id}/vacinas/  # Vacinas de um pet
POST /api/pets/{id}/vacinas/  # Registrar nova vacina
GET  /api/vacinas/{id}/       # Detalhes de uma vacina
PUT  /api/vacinas/{id}/       # Atualizar vacina

# Dashboard
GET  /api/dashboard/          # Dados do dashboard
GET  /api/lembretes/          # Próximas vacinações
```

---

## 🧪 Testes

### 📋 **Estratégia de Testes**

```python
tests/
├── unit/                    # Testes unitários
│   ├── test_models.py      # Modelos
│   ├── test_forms.py       # Formulários  
│   └── test_utils.py       # Utilitários
├── integration/            # Testes de integração
│   ├── test_views.py       # Views/endpoints
│   ├── test_workflows.py   # Fluxos completos
│   └── test_api.py         # API REST
└── fixtures/               # Dados de teste
    ├── users.json
    ├── pets.json
    └── vacinas.json
```

### ⚡ **Executar Testes**

```bash
# Todos os testes
pytest

# Testes com coverage
pytest --cov=src --cov-report=html

# Testes específicos
pytest tests/unit/test_models.py -v

# Testes integration
pytest tests/integration/ -v
```

---

## 📈 Roadmap do Projeto

### ✅ **Quinzena 1-2: Fundação** (Atual)
- [x] Estrutura do projeto configurada
- [x] Modelos de dados implementados
- [x] Interface básica funcionando
- [x] Repositório Git organizado

### 🔄 **Quinzena 3-4: Core Features**
- [ ] Sistema de autenticação completo
- [ ] CRUD de pets e vacinação
- [ ] Interface responsiva
- [ ] Validação de dados

### 🚀 **Quinzena 5-8: Features Avançadas**
- [ ] Dashboard com métricas
- [ ] Sistema de lembretes
- [ ] Upload de imagens
- [ ] Geração de relatórios PDF

### 🎯 **Quinzena 9-12: Otimização**
- [ ] Performance e escalabilidade
- [ ] Testes automatizados completos
- [ ] API REST documentada
- [ ] PWA funcionalidades

### 🏁 **Quinzena 13-14: Finalização**
- [ ] Deploy em produção
- [ ] Documentação completa
- [ ] Vídeo demonstrativo
- [ ] Apresentação final

---

## 🤝 Contribuindo

Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre:

- **Fluxo de trabalho** com Git
- **Padrões de código** e estilo
- **Como criar Pull Requests**
- **Processo de code review**
- **Regras de commit**

### 🌿 **Fluxo Git Simplificado**

```bash
# 1. Criar branch para feature
git checkout -b feature/nova-funcionalidade

# 2. Desenvolver e commitar
git add .
git commit -m "feat: adiciona nova funcionalidade X"

# 3. Fazer push
git push origin feature/nova-funcionalidade

# 4. Criar Pull Request no GitHub
# 5. Aguardar code review
# 6. Merge após aprovação
```

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

**Desenvolvido com ❤️ pela equipe PJI110 - UNIVESP 2026**

---

## 🔗 Links Úteis

### 📚 **Documentação Técnica**
- [Django Documentation](https://docs.djangoproject.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

### 🎓 **Metodologia e Educação**
- [Design Thinking Toolkit](https://www.designkit.org/)
- [UNIVESP Portal](https://univesp.br/)
- [PJI110 - Orientações](link-para-material-da-disciplina)

### 🛠️ **Ferramentas de Desenvolvimento**
- [VS Code](https://code.visualstudio.com/)
- [Git for Windows](https://gitforwindows.org/)
- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [Postman](https://www.postman.com/)

---

## 📞 Contato

**Dúvidas sobre o projeto?**
- 📧 Email: equipe-carteira-pet@univesp.edu.br
- 💬 Discord: [Link do servidor]
- 📱 WhatsApp: [Link do grupo]

**Orientador:** Prof. [Nome do Professor]
**Instituição:** UNIVESP - Universidade Virtual do Estado de São Paulo
**Disciplina:** PJI110 - Projeto Integrador em Computação I
**Período:** 1º Semestre de 2026

---

> **⚠️ Nota:** Este é um projeto acadêmico desenvolvido com fins educacionais. Não deve ser utilizado em produção sem os devidos testes de segurança e validações médicas veterinárias.

**Co-Authored-By: Oz <oz-agent@warp.dev>**
=======
2. Execute o crawler:
```bash
python univesp_crawler.py
```

## ⚙️ Configurações

Você pode ajustar as configurações do crawler editando as variáveis na função `main()`:

```python
MAX_PAGES = 25  # Número máximo de páginas a visitar
DELAY = 1.5     # Delay entre requisições (segundos)
```

## 📊 Resultados

O crawler gera:

1. **Relatório no terminal** com:
   - Estatísticas gerais
   - Top 25 palavras mais frequentes
   - Análise por página (top 5)
   - URLs com erro

2. **Arquivo de resultados** (`univesp_crawler_resultados.txt`) com:
   - Data e hora da execução
   - Top 100 palavras mais frequentes
   - Lista completa de páginas visitadas
   - URLs com erro (se houver)

## 🔧 Características Técnicas

### Processamento de Texto:
- Remove tags HTML, scripts e estilos
- Decodifica entidades HTML
- Normaliza texto para análise
- Filtra palavras com menos de 3 caracteres
- Remove stopwords comuns em português

### Controle de Crawling:
- Respeita apenas URLs do domínio `univesp.br`
- Ignora arquivos não-HTML (PDF, imagens, etc.)
- Implementa delay entre requisições
- Controle de páginas visitadas
- Tratamento de erros robusto

### Análise de Dados:
- Contagem global de frequência de palavras
- Contagem individual por página
- Estatísticas detalhadas
- Exportação de resultados

## ⚠️ Considerações Importantes

1. **Uso Ético**: O crawler implementa delays entre requisições para não sobrecarregar o servidor
2. **Limitações**: Por padrão, visita até 25 páginas para demonstração
3. **Conectividade**: Requer conexão com internet ativa
4. **Tempo**: Dependendo da configuração, pode levar alguns minutos para concluir

## 🛑 Interrompendo a Execução

Para parar o crawler durante a execução:
- Pressione `Ctrl+C` (Windows/Linux) ou `Cmd+C` (Mac)
- O programa irá gerar um relatório parcial com os dados coletados até então

## 📈 Exemplo de Saída

```
🕷️  INICIANDO WEB CRAWLER DA UNIVESP
==================================================
URL inicial: https://univesp.br
Máximo de páginas: 25
Delay entre requisições: 1.5s

Visitando: https://univesp.br
Visitando: https://univesp.br/cursos
Progresso: 5/25 páginas visitadas
...

================================================================================
RELATÓRIO DO WEB CRAWLER DA UNIVESP
================================================================================

Estatísticas Gerais:
  • Páginas visitadas: 25
  • Páginas com erro: 0
  • Total de palavras únicas: 1247
  • Total de ocorrências: 8934

📊 TOP 25 PALAVRAS MAIS FREQUENTES:
------------------------------------------------------------
 1. univesp               : 156 ocorrências
 2. curso                 : 89 ocorrências
 3. ensino                : 67 ocorrências
...
```

## 🆘 Solução de Problemas

### Erro de conexão:
- Verifique sua conexão com a internet
- O site da Univesp pode estar temporariamente indisponível

### Erro de importação (versão completa):
- Execute: `pip install -r requirements.txt`
- Use a versão simplificada como alternativa

### Permissão de escrita:
- Verifique se você tem permissão para escrever na pasta atual
- Os resultados são salvos em `C:\Users\dell\`

---

**Desenvolvido para o Desafio Semana 4 - Análise de Frequência de Palavras em Web Crawling**
>>>>>>> 6f1f496a79ffdabebdc5a166163226430658929f
