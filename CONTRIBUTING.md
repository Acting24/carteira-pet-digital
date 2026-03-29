# 🤝 Guia de Contribuição - Carteira Digital Pet

**PJI110 - UNIVESP 2026**  
**Repositório:** https://github.com/Acting24/carteira-pet-digital

Obrigado por contribuir com o projeto **Carteira Digital Pet**! Este guia vai te ajudar a colaborar de forma eficiente e seguir nossos padrões de qualidade.

---

## 🎯 **Como Contribuir**

### **👥 Nossa Equipe (7 Integrantes)**

| Integrante | Nome | Email | Área Principal | GitHub |
|------------|------|-------|----------------|--------|
| **1** | Adilson Lucas da Silva | 24205869@aluno.univesp.br | 🎯 Líder/Repository Owner | Acting24 |
| **2** | David Wilames Nunes Batista | 23217049@aluno.univesp.br | 🏗️ Arquiteto/Tech Lead | ? |
| **3** | Helton Silva de Almeida | 24209102@aluno.univesp.br | ⚙️ Desenvolvedor Backend | ? |
| **4** | Lucas Pereira de Lima | 24214565@aluno.univesp.br | 🗄️ Especialista BD | ? |
| **5** | Thaise Michelaine Nunes de Oliveira | 24219760@aluno.univesp.br | 🎨 Desenvolvedora Frontend/UX | ? |
| **6** | Vanessa de Pádua Nunes Fusco Parisi | 24219706@aluno.univesp.br | 👥 UX Researcher | ? |
| **7** | Vanessa Dias Fernandes | 24202074@aluno.univesp.br | 📚 Documentadora/QA | ? |

---

## 🚀 **Primeiros Passos**

### **1. 🔧 Configuração Inicial**

```bash
# 1. Clonar repositório
git clone https://github.com/Acting24/carteira-pet-digital.git
cd carteira-pet-digital

# 2. Configurar Git (se ainda não fez)
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu.email@aluno.univesp.br"

# 3. Verificar estrutura
ls -la
```

### **2. 🌿 Criar Branch para Sua Contribuição**

```bash
# Sempre partir do develop atualizado
git checkout main
git pull origin main
git checkout develop
git pull origin develop

# Criar sua branch seguindo convenção
git checkout -b tipo/nome-da-funcionalidade

# Exemplos:
git checkout -b feature/cadastro-pet
git checkout -b fix/erro-idade-calculo
git checkout -b docs/atualizacao-readme
git checkout -b style/melhorias-css
```

---

## 📚 **Convenções e Padrões**

### **🌿 Nomenclatura de Branches**

#### **Padrão:**
```
tipo/descricao-curta-kebab-case
```

#### **Tipos Aceitos:**
- **`feature/`** - Nova funcionalidade
- **`fix/`** - Correção de bug
- **`docs/`** - Documentação
- **`style/`** - CSS, formatação visual
- **`refactor/`** - Refatoração de código
- **`test/`** - Testes
- **`chore/`** - Tarefas de manutenção

#### **Exemplos Corretos:**
```bash
feature/sistema-login
feature/upload-foto-pet
fix/calculo-idade-pet
fix/erro-formulario-cadastro
docs/instalacao-windows
docs/guia-contribuicao
style/responsivo-mobile
style/cores-tema-principal
refactor/models-django
test/validacao-forms
chore/atualizacao-dependencies
```

### **📝 Mensagens de Commit (Conventional Commits)**

#### **Formato:**
```
tipo(escopo): descrição curta em português

- Detalhe opcional 1
- Detalhe opcional 2
- Detalhe opcional 3

PJI110-UNIVESP-2026
Co-Authored-By: Nome do Colaborador <email@aluno.univesp.br>
```

#### **Tipos:**
- **`feat`** - Nova funcionalidade
- **`fix`** - Correção de bug
- **`docs`** - Documentação
- **`style`** - Formatação (sem mudança de lógica)
- **`refactor`** - Refatoração
- **`test`** - Testes
- **`chore`** - Manutenção

#### **Escopos Sugeridos:**
- `pets` - Funcionalidades relacionadas a pets
- `auth` - Sistema de autenticação
- `users` - Gestão de usuários
- `vets` - Veterinários
- `vaccines` - Sistema de vacinas
- `ui` - Interface do usuário
- `db` - Banco de dados
- `api` - APIs
- `docs` - Documentação
- `config` - Configurações

#### **Exemplos Práticos:**

```bash
feat(pets): adiciona formulário de cadastro de pet

- Implementa validação de campos obrigatórios
- Adiciona upload de foto com preview
- Inclui seleção de espécie (canina, felina, etc)
- Calcula idade automaticamente baseada na data de nascimento
- Adiciona validação de microchip único

PJI110-UNIVESP-2026
```

```bash
fix(auth): corrige bug no login com email

- Resolve erro de case sensitivity no email
- Melhora mensagens de erro para usuário
- Adiciona validação de formato de email
- Corrige redirecionamento após login

PJI110-UNIVESP-2026
Co-Authored-By: David Wilames <23217049@aluno.univesp.br>
```

```bash
docs(readme): atualiza instruções de instalação

- Adiciona seção específica para Windows
- Melhora exemplos de comandos
- Corrige links quebrados para documentação
- Adiciona troubleshooting comum

PJI110-UNIVESP-2026
```

---

## 🏗️ **Estrutura do Projeto**

### **📁 Organização de Pastas**

```
carteira-pet-digital/
├── 📚 docs/                          # Documentação
│   ├── requisitos/                   # Análise de requisitos
│   │   └── Analise_Requisitos.md
│   ├── wireframes/                   # Protótipos (Integrante 5)
│   ├── diagramas/                    # ER e arquitetura (Integrante 4)
│   ├── design_thinking/              # Fase Empatia (Integrante 6)
│   └── referencias/                  # Bibliografia ABNT
│
├── 🥇 django_app/                    # DJANGO (Principal)
│   ├── carteira_pet/                 # Configurações projeto
│   │   ├── settings.py               # Configurações principais
│   │   ├── urls.py                   # URLs principais
│   │   └── wsgi.py                   # Deploy
│   ├── apps/                         # Apps modulares
│   │   ├── core/                     # App principal
│   │   │   ├── models.py             # Usuario, Tutor, Veterinario
│   │   │   ├── views.py              # Views principais
│   │   │   └── admin.py              # Django Admin
│   │   ├── pets/                     # App pets
│   │   │   ├── models.py             # Pet, Especie, PetVeterinario
│   │   │   ├── forms.py              # Formulários
│   │   │   ├── views.py              # Views pets
│   │   │   └── templates/            # Templates específicos
│   │   └── vacinas/                  # App vacinas
│   │       ├── models.py             # Vacina
│   │       ├── views.py              # Views vacinas
│   │       └── templates/
│   ├── static/                       # CSS, JS, imagens globais
│   ├── templates/                    # Templates base
│   └── media/                        # Uploads (fotos pets)
│
├── 🥈 src/                           # FLASK (Alternativa)
│   └── app/
│       ├── models/                   # SQLAlchemy models
│       ├── routes/                   # Blueprints
│       ├── templates/                # Jinja2 templates
│       └── static/                   # CSS/JS Flask
│
├── 📋 tests/                         # Testes automatizados
│   ├── test_models.py
│   ├── test_views.py
│   └── test_integration.py
│
├── 📄 Arquivos Principais
│   ├── README.md                     # Manual do projeto
│   ├── CONTRIBUTING.md               # Este arquivo
│   ├── CODE_OF_CONDUCT.md           # Código de conduta
│   ├── CURSO_GIT_GITHUB_EQUIPE.md   # Curso Git/GitHub
│   ├── requirements.txt              # Dependências Flask
│   ├── requirements-django.txt       # Dependências Django
│   ├── .gitignore                    # Arquivos ignorados
│   └── config.py                     # Configurações Flask
```

---

## 👨‍💻 **Processo de Desenvolvimento**

### **🔄 Fluxo Completo (GitFlow)**

#### **1. 📋 Planejamento**
- Verificar Issues abertas no GitHub
- Discutir implementação no WhatsApp
- Definir responsável e prazo
- Atualizar status no projeto

#### **2. 🌿 Desenvolvimento**
```bash
# Partir do develop atualizado
git checkout develop
git pull origin develop

# Criar branch específica
git checkout -b feature/nome-funcionalidade

# Desenvolver funcionalidade
# (fazer alterações nos arquivos)

# Testar localmente
python manage.py runserver  # Django
# ou
python run.py               # Flask

# Commit frequente (a cada funcionalidade pequena)
git add .
git commit -m "feat(escopo): descrição do que foi feito"
```

#### **3. 🧪 Testes**
```bash
# Testar funcionalidade implementada
python manage.py test        # Django
pytest                       # Flask

# Verificar linting
flake8 .                     # Python style
black .                      # Code formatting

# Testar instalação fresh
pip install -r requirements.txt
```

#### **4. 📤 Pull Request**
```bash
# Push da branch
git push origin feature/nome-funcionalidade

# No GitHub:
# 1. Criar Pull Request
# 2. Preencher template
# 3. Marcar revisor
# 4. Aguardar aprovação
```

#### **5. 🔍 Code Review**
- Revisor analisa código
- Testa localmente se necessário
- Comenta melhorias
- Aprova ou solicita alterações

#### **6. 🔄 Merge**
```bash
# Após aprovação:
# 1. Merge no develop (GitHub)
# 2. Delete branch (GitHub)
# 3. Atualizar local
git checkout develop
git pull origin develop
git branch -d feature/nome-funcionalidade
```

---

## 🎯 **Áreas de Contribuição**

### **🏗️ Backend (Django Principal)**

#### **Responsáveis:** Helton Silva + Lucas Pereira
#### **Tecnologias:** Python, Django, MySQL/SQLite

**Como Contribuir:**
```bash
# 1. Trabalhar na pasta django_app/
cd django_app/

# 2. Ativar ambiente virtual
python -m venv venv
venv\Scripts\activate              # Windows
source venv/bin/activate           # Linux/Mac

# 3. Instalar dependências
pip install -r requirements-django.txt

# 4. Rodar migrações
python manage.py makemigrations
python manage.py migrate

# 5. Testar servidor
python manage.py runserver
```

**Padrões Backend:**
- Models bem documentados
- Views baseadas em classe quando apropriado
- Serializers para APIs
- Testes unitários para models e views
- Validações customizadas nos forms
- Admin interface configurada

### **🎨 Frontend/UX (Templates e CSS)**

#### **Responsáveis:** Thaise Michelaine + Vanessa de Pádua
#### **Tecnologias:** HTML5, CSS3, JavaScript, Bootstrap 5

**Como Contribuir:**
```bash
# 1. Trabalhar em templates e static files
django_app/templates/
django_app/static/
src/app/templates/              # Flask alternativo
src/app/static/

# 2. Testar responsividade
# - Mobile first design
# - Testar em diferentes browsers
# - Validar acessibilidade básica
```

**Padrões Frontend:**
- Bootstrap 5.3 como base
- CSS customizado organizado
- JavaScript ES6+
- Templates responsivos
- Componentes reutilizáveis
- Ícones Font Awesome
- Formulários com validação client-side

### **📚 Documentação**

#### **Responsáveis:** Vanessa Dias + David Wilames
#### **Tecnologias:** Markdown, Diagramas

**Como Contribuir:**
```bash
# 1. Trabalhar na pasta docs/
docs/requisitos/
docs/wireframes/
docs/diagramas/
docs/design_thinking/

# 2. Manter arquivos principais atualizados
README.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
```

**Padrões Documentação:**
- Markdown com emojis para visual
- Imagens em pasta docs/images/
- Links sempre funcionais
- Exemplos práticos
- Linguagem clara e objetiva

### **🗄️ Banco de Dados**

#### **Responsável:** Lucas Pereira
#### **Tecnologias:** MySQL (produção), SQLite (desenvolvimento)

**Como Contribuir:**
```bash
# 1. Trabalhar com models Django
django_app/apps/core/models.py
django_app/apps/pets/models.py
django_app/apps/vacinas/models.py

# 2. Ou models SQLAlchemy (Flask)
src/app/models/
```

**Padrões Banco:**
- Models bem relacionados
- Validações no nível do banco
- Índices apropriados
- Migrations versionadas
- Backup/restore documentado

---

## ✅ **Checklist de Qualidade**

### **📋 Antes de Fazer Commit**

- [ ] **Código funciona** localmente
- [ ] **Testes passam** (se existirem)
- [ ] **Sem erros** de linting
- [ ] **Documentação** atualizada se necessário
- [ ] **Commit message** seguindo convenção
- [ ] **Arquivos desnecessários** não incluídos

### **📋 Antes de Pull Request**

- [ ] **Branch atualizada** com develop
- [ ] **Conflitos resolvidos**
- [ ] **Descrição clara** do que foi implementado
- [ ] **Screenshots** se mudança visual
- [ ] **Revisor marcado**
- [ ] **Issues relacionadas** linkadas

### **📋 Para Code Review**

- [ ] **Código legível** e bem estruturado
- [ ] **Segue padrões** do projeto
- [ ] **Performance** adequada
- [ ] **Segurança** considerada
- [ ] **Funcionalidade testada**
- [ ] **Documentação necessária**

---

## 🛠️ **Ferramentas Recomendadas**

### **💻 Editores**
- **Visual Studio Code** (recomendado)
  - Extensão: GitLens
  - Extensão: Python
  - Extensão: Django
  - Extensão: Prettier
  - Extensão: Auto Rename Tag

- **PyCharm** (alternativo)
- **Sublime Text** (leve)

### **🔧 Git Clients**
- **Terminal** (recomendado)
- **SourceTree** (visual)
- **GitHub Desktop** (simples)

### **🧪 Testing**
```bash
# Django
python manage.py test

# Flask  
pytest

# Coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📞 **Onde Buscar Ajuda**

### **🆘 Canais de Suporte**

#### **🟢 Dúvidas Rápidas:**
- **WhatsApp do Grupo** (resposta rápida)
- **GitHub Issues** (para documentar)

#### **🟡 Problemas Técnicos:**
- **David Wilames** (Tech Lead): 23217049@aluno.univesp.br
- **Adilson Lucas** (Repository Owner): 24205869@aluno.univesp.br

#### **🔴 Problemas Graves:**
- **Issues no GitHub** com label "bug" ou "help wanted"
- **WhatsApp + @everyone**

### **📚 Recursos de Aprendizado**

#### **Django:**
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Real Python Django](https://realpython.com/tutorials/django/)

#### **Git/GitHub:**
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

#### **Nosso Projeto:**
- **README.md** - Manual completo
- **CURSO_GIT_GITHUB_EQUIPE.md** - Curso interno
- **Issues GitHub** - Discussões técnicas

---

## 🎉 **Reconhecimento de Contribuições**

### **🌟 Como Reconhecemos Contribuições**

#### **📊 Métricas de Contribuição:**
- **Commits regulares** e bem documentados
- **Pull Requests** de qualidade
- **Code Reviews** construtivos
- **Documentação** melhorada
- **Bugs resolvidos**
- **Ajuda aos colegas**

#### **🏆 Reconhecimentos:**
- **Menção nos commits** com Co-Authored-By
- **Destaque no README.md** para contribuições especiais
- **Issues assignment** para áreas de expertise
- **Tech leadership** em funcionalidades específicas

---

## 📝 **Templates Úteis**

### **🔄 Template de Pull Request**

```markdown
## 📋 Descrição
Breve descrição do que foi implementado

## 🎯 Tipo de Mudança
- [ ] Nova funcionalidade (feature)
- [ ] Correção de bug (fix)
- [ ] Documentação
- [ ] Refatoração
- [ ] Melhoria de performance

## ✅ Checklist
- [ ] Código testado localmente
- [ ] Testes passando
- [ ] Documentação atualizada
- [ ] Commits seguem convenção

## 📸 Screenshots (se aplicável)
Adicionar imagens se mudança visual

## 🔗 Issues Relacionadas
Fixes #123
Related to #456

## 👀 Revisor Sugerido
@github-username
```

### **🐛 Template de Issue (Bug)**

```markdown
## 🐛 Descrição do Bug
Descrição clara do problema

## 🔄 Como Reproduzir
1. Ir para página X
2. Clicar em Y
3. Ver erro Z

## ✅ Comportamento Esperado
O que deveria acontecer

## 📸 Screenshots
Adicionar se necessário

## 🖥️ Ambiente
- OS: Windows/Linux/Mac
- Browser: Chrome/Firefox/Safari
- Versão do Python: 3.x
```

---

## 🎯 **Conclusão**

### **💪 Nossa Meta**

> **"Contribuir com excelência técnica e colaboração respeitosa para criar o melhor sistema de Carteira Digital Pet da UNIVESP 2026!"**

### **📈 Métricas de Sucesso**
- **100% da equipe** contribuindo regularmente
- **Zero conflitos** não resolvidos
- **Código de qualidade** sempre
- **Documentação atualizada**
- **Entrega no prazo**

### **🎓 Aprendizado Contínuo**
- Crescer tecnicamente juntos
- Compartilhar conhecimento
- Aplicar boas práticas
- Preparar para mercado de trabalho

---

**🚀 VAMOS JUNTOS CRIAR ALGO INCRÍVEL! 🚀**

**PJI110 - UNIVESP 2026**  
**Equipe Carteira Digital Pet**

---

> **Criado por:** David Wilames Nunes Batista (Tech Lead)  
> **Revisado por:** Adilson Lucas da Silva (Repository Owner)  
> **Co-Authored-By:** Oz <oz-agent@warp.dev>

**📅 Data:** 29/03/2026  
**📊 Versão:** 1.0  
**🎯 Status:** Ativo e pronto para uso!