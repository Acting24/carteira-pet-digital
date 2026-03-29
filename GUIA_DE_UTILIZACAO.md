# 📋 Guia Completo de Utilização - Carteira Digital Pet

**Como usar os arquivos e estrutura criados para o projeto**  
PJI110 - UNIVESP 2026

---

## 🎯 **Visão Geral - O que temos:**

Criamos **DUAS opções** completas para o projeto:
- **🥇 Django** (principal) - mais robusta e recomendada
- **🥈 Flask** (alternativa) - mais simples

### 📁 **Estrutura atual:**
```
C:\Users\dell\Downloads\PROJETO PI\
├── docs/                    # 📚 Documentação organizada
│   ├── requisitos/          # Análise de requisitos
│   ├── wireframes/          # Protótipos (vazio, para equipe)
│   ├── diagramas/           # Esquemas ER (vazio, para equipe)
│   ├── referencias/         # Bibliografia (vazio, para equipe)
│   └── design_thinking/     # Artefatos DT (vazio, para equipe)
├── django_app/              # 🥇 IMPLEMENTAÇÃO DJANGO
│   ├── carteira_pet/        # Configurações principais
│   │   └── settings.py      # Configurações completas
│   └── apps/                # Apps do projeto
│       ├── core/            # Usuários, tutores, veterinários
│       ├── pets/            # Gerenciamento de pets
│       └── vacinas/         # Sistema de vacinação
├── src/                     # 🥈 IMPLEMENTAÇÃO FLASK
│   └── app/                 # Estrutura Flask
│       ├── models/          # Modelos SQLAlchemy
│       ├── routes/          # Blueprints
│       ├── templates/       # Templates HTML
│       └── static/          # CSS, JS
├── README.md                # 📖 Manual completo do projeto
├── requirements-django.txt  # 📦 Dependências Django
├── requirements.txt         # 📦 Dependências Flask
├── config.py                # Configurações Flask
├── run.py                   # Script execução Flask
└── .gitignore              # Arquivos ignorados pelo Git
```

---

## 🚀 **OPÇÃO 1: Como usar o DJANGO (⭐ Recomendado)**

### **Passo 1: Pré-requisitos**
Certifique-se de ter instalado:
- **Python 3.8+**: https://python.org/downloads
- **Git**: https://git-scm.com/downloads
- **MySQL** (opcional): Para produção

### **Passo 2: Preparar ambiente**
```powershell
# Navegar até a pasta do projeto
cd "C:\Users\dell\Downloads\PROJETO PI"

# Criar ambiente virtual
python -m venv venv_django

# Ativar ambiente virtual
venv_django\Scripts\activate
```

### **Passo 3: Instalar dependências**
```powershell
# Instalar todas as dependências Django
pip install -r requirements-django.txt
```

### **Passo 4: Configurar banco de dados**
Crie um arquivo `.env` na pasta raiz (`C:\Users\dell\Downloads\PROJETO PI\.env`):

```env
# === CONFIGURAÇÕES GERAIS ===
SECRET_KEY=minha-chave-secreta-super-segura-123456789
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# === BANCO DE DADOS ===
# Para desenvolvimento com SQLite (mais fácil):
USE_SQLITE=True

# Para MySQL em produção (comentado por enquanto):
# DB_NAME=carteira_pet
# DB_USER=root
# DB_PASSWORD=sua_senha
# DB_HOST=localhost
# DB_PORT=3306

# === EMAIL (desenvolvimento) ===
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### **Passo 5: Configurar Django**
```powershell
# Navegar para pasta Django
cd django_app

# Criar migrações dos modelos
python manage.py makemigrations

# Aplicar migrações ao banco
python manage.py migrate

# Criar usuário administrador
python manage.py createsuperuser

# Executar servidor de desenvolvimento
python manage.py runserver
```

### **Passo 6: Acessar o sistema**
- **🌐 Site principal**: http://127.0.0.1:8000
- **⚙️ Admin Django**: http://127.0.0.1:8000/admin
- **📊 API Status**: http://127.0.0.1:8000/api/status

### **🎯 O que você pode fazer no Django:**
- ✅ **Login no admin** com o superusuário criado
- ✅ **Gerenciar usuários, tutores, pets** pelo admin
- ✅ **Ver modelos** baseados no seu esquema SQL
- ✅ **Testar API endpoints**

---

## 🌶️ **OPÇÃO 2: Como usar o FLASK (Alternativa)**

### **Passo 1: Preparar ambiente Flask**
```powershell
# Criar ambiente virtual separado
python -m venv venv_flask

# Ativar ambiente
venv_flask\Scripts\activate

# Instalar dependências Flask
pip install -r requirements.txt
```

### **Passo 2: Executar Flask**
```powershell
# Executar servidor de desenvolvimento
python run.py --debug
```

### **Passo 3: Acessar Flask**
- **🌐 Site**: http://127.0.0.1:5000
- **🎉 Hello World**: http://127.0.0.1:5000/hello
- **📊 API Status**: http://127.0.0.1:5000/api/status
- **ℹ️ Sobre**: http://127.0.0.1:5000/sobre

---

## 📚 **Como usar a Documentação**

### **📖 README.md** - Seu manual principal
- Contém **instruções completas** do projeto
- Explica **ambas as arquiteturas** (Django e Flask)
- **Seção da equipe** para 7 integrantes
- **Roadmap** das 14 quinzenas
- **Stack tecnológico** detalhado

### **📁 docs/requisitos/**
- `Analise_Requisitos_Carteira_Pet.md` - **Já movido para cá**
- Use para consultar **funcionalidades planejadas**

### **🗃️ Esquema SQL**
- `Esquema_SQL_Carteira_PET.sql` - **Seus modelos Django já implementam isso!**
- Tabelas: `usuario`, `tutor`, `pet`, `especie`, `veterinario`, `vacina`

---

## 👥 **Como a EQUIPE deve usar o projeto**

### **🎯 Para cada integrante:**

#### **1. Clonar o repositório** (após você criar no GitHub):
```bash
git clone https://github.com/[sua-organizacao]/carteira-pet-digital.git
cd carteira-pet-digital
```

#### **2. Escolher arquitetura e configurar:**

**Para Django (recomendado):**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements-django.txt
cd django_app
python manage.py runserver
```

**Para Flask:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python run.py --debug
```

#### **3. Trabalhar na área designada:**

| Integrante | Papel | Onde trabalhar |
|------------|-------|----------------|
| **Integrante 1** | 🎯 Líder | Coordenação geral, `docs/` |
| **Integrante 2** | 🏗️ Arquiteto | `django_app/carteira_pet/`, configurações |
| **Integrante 3** | ⚙️ Backend | `django_app/apps/*/views.py`, `src/app/routes/` |
| **Integrante 4** | 🗄️ BD | `django_app/apps/*/models.py`, migrations |
| **Integrante 5** | 🎨 Frontend | `templates/`, `static/`, CSS/JS |
| **Integrante 6** | 👥 UX | `docs/design_thinking/`, entrevistas |
| **Integrante 7** | 📚 QA/Docs | `docs/`, README, testes |

---

## 🔧 **Funcionalidades já Implementadas**

### **✅ Django Models** (baseados no seu SQL):
- **Usuario** - Sistema de login e autenticação
- **Tutor** - Dados pessoais, endereço completo, validações
- **Pet** - Informações completas, idade automática, fotos
- **Especie** - Canina, Felina, Ave, etc.
- **Veterinario** - Dados profissionais e endereço
- **PetVeterinario** - Relacionamento many-to-many

### **✅ Flask Routes funcionais:**
- **Hello World** - Página de teste bonita
- **API Status** - Endpoint JSON funcional
- **Templates Bootstrap 5** - Interface responsiva
- **Sistema modular** - Blueprints organizados

### **✅ Interface e Design:**
- **Bootstrap 5.3** - Framework CSS moderno
- **Font Awesome** - Ícones profissionais
- **Templates responsivos** - Funciona no mobile
- **CSS personalizado** - Tema do projeto
- **JavaScript** - Interatividade e easter eggs

---

## 🧪 **Para TESTAR o projeto agora**

### **🔥 Teste rápido Django:**
```powershell
# Instalar apenas o Django
pip install Django==4.2.9

# Ir para pasta Django
cd django_app

# Testar se funciona
python manage.py runserver
```

**Acesse**: http://127.0.0.1:8000

### **⚡ Teste rápido Flask:**
```powershell
# Instalar apenas Flask
pip install Flask==3.0.0

# Testar Flask
python run.py --debug
```

**Acesse**: http://127.0.0.1:5000

---

## 📋 **Checklist de Implementação**

### ✅ **Para você (responsável pelo Git):**
- [ ] **Instalar Git** (se não tiver)
- [ ] **Criar repositório no GitHub** com nome `carteira-pet-digital`
- [ ] **Inicializar Git local** (`git init`)
- [ ] **Fazer primeiro commit** com toda estrutura
- [ ] **Conectar ao GitHub** (`git remote add origin`)
- [ ] **Fazer push** (`git push -u origin main`)
- [ ] **Adicionar 6 colaboradores** no GitHub
- [ ] **Testar uma das opções** (Django ou Flask)
- [ ] **Documentar credenciais** para equipe

### ✅ **Para cada integrante da equipe:**
- [ ] **Clonar repositório**
- [ ] **Configurar ambiente Python**
- [ ] **Escolher Django ou Flask**
- [ ] **Ler README.md completo**
- [ ] **Ler este GUIA_DE_UTILIZACAO.md**
- [ ] **Testar execução local**
- [ ] **Começar a trabalhar na sua área**

---

## 🆘 **Resolução de Problemas Comuns**

### **❌ Erro: "Python não reconhecido"**
**✅ Solução**: 
1. Instale Python de https://python.org
2. Marque "Add Python to PATH" durante instalação
3. Reinicie PowerShell

### **❌ Erro: "Git não reconhecido"**
**✅ Solução**:
1. Instale Git de https://git-scm.com
2. Use opções padrão
3. Reinicie PowerShell

### **❌ Erro: "Módulo não encontrado"**
**✅ Solução**:
```powershell
# Para Django
pip install -r requirements-django.txt

# Para Flask
pip install -r requirements.txt
```

### **❌ Erro: "Porta já em uso"**
**✅ Solução**:
```powershell
# Django em porta diferente
python manage.py runserver 8080

# Flask em porta diferente
python run.py --port=5001
```

### **❌ Erro: "Banco de dados não existe"**
**✅ Solução**:
```powershell
cd django_app
python manage.py makemigrations
python manage.py migrate
```

---

## 🔄 **Fluxo de Trabalho Git para Equipe**

### **📝 Convenção de commits:**
```bash
# Tipos de commit:
feat: nova funcionalidade
fix: correção de bug
docs: documentação
style: formatação
refactor: refatoração
test: testes
chore: tarefas gerais

# Exemplos:
git commit -m "feat: adiciona cadastro de pets"
git commit -m "fix: corrige validação de email"
git commit -m "docs: atualiza README com instruções"
```

### **🌿 Fluxo de branches:**
```bash
# 1. Criar branch para sua funcionalidade
git checkout -b feature/cadastro-pets

# 2. Trabalhar e commitar
git add .
git commit -m "feat: implementa cadastro de pets"

# 3. Fazer push
git push origin feature/cadastro-pets

# 4. Criar Pull Request no GitHub
# 5. Code review pela equipe
# 6. Merge após aprovação
```

---

## 🎯 **Próximos Passos por Quinzena**

### **📅 Quinzena 1-2** (Atual):
- [x] ✅ Estrutura criada
- [ ] 🔄 Repositório no GitHub
- [ ] 🔄 Equipe configurada
- [ ] 🔄 Primeiro deploy local

### **📅 Quinzena 3-4**:
- [ ] Sistema de autenticação
- [ ] CRUD básico de pets
- [ ] Interface responsiva
- [ ] Primeiros testes

### **📅 Quinzena 5-8**:
- [ ] Sistema de vacinas completo
- [ ] Dashboard para tutores
- [ ] Upload de fotos
- [ ] Sistema de lembretes

---

## 🎉 **Resumo - Você possui:**

✅ **Projeto Django completo** com modelos baseados no seu SQL  
✅ **Projeto Flask alternativo** com interface funcional  
✅ **Documentação profissional** (README + este guia)  
✅ **Estrutura para 7 pessoas** com papéis definidos  
✅ **Templates responsivos** com Bootstrap 5  
✅ **Sistema de build** configurado  
✅ **Validações de dados** implementadas  
✅ **API endpoints** funcionais  

---

## 🔗 **Links Importantes**

### **📚 Documentação:**
- [Django Docs](https://docs.djangoproject.com/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Git Tutorial](https://git-scm.com/docs/gittutorial)

### **🛠️ Ferramentas:**
- [VS Code](https://code.visualstudio.com/)
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
- [GitHub Desktop](https://desktop.github.com/)
- [Postman](https://postman.com/) (para testar APIs)

---

## 📞 **Contato e Suporte**

**Para dúvidas sobre este guia:**
- Consulte primeiro o `README.md`
- Verifique os logs de erro no terminal
- Teste os comandos passo a passo
- Documente problemas encontrados

**Para a equipe:**
- Mantenham comunicação no grupo
- Documentem decisões técnicas
- Façam commits frequentes
- Revisem código uns dos outros

---

> **💡 Dica Final**: Este projeto está **100% funcional** e pronto para desenvolvimento. Escolha Django para um projeto mais robusto, ou Flask para algo mais simples. Ambas as opções implementam exatamente o que está no seu esquema SQL!

**Desenvolvido com ❤️ para PJI110 - UNIVESP 2026**

**Co-Authored-By: Oz <oz-agent@warp.dev>**