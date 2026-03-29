# 🔐 Credenciais e Informações da Equipe - Carteira Digital Pet

**PJI110 - UNIVESP 2026**  
**Disciplina:** Projeto Integrador em Computação I  
**Projeto:** Sistema web para gerenciamento de vacinação de pets

---

## 📋 **Informações do Repositório**

### 🗂️ **GitHub Repository**
- **Nome:** `carteira-pet-digital`
- **URL:** `https://github.com/[SEU_USUARIO]/carteira-pet-digital`
- **Branch Principal:** `main`
- **Visibilidade:** Público

### 👥 **Colaboradores do Repositório**
| Integrante | GitHub Username | Email | Papel |
|------------|----------------|-------|-------|
| **Integrante 1** | `@usuario1` | email1@exemplo.com | 🎯 Líder / Product Owner |
| **Integrante 2** | `@usuario2` | email2@exemplo.com | 🏗️ Arquiteto / Tech Lead |
| **Integrante 3** | `@usuario3` | email3@exemplo.com | ⚙️ Desenvolvedor Backend |
| **Integrante 4** | `@usuario4` | email4@exemplo.com | 🗄️ Especialista BD |
| **Integrante 5** | `@usuario5` | email5@exemplo.com | 🎨 Desenvolvedor Frontend/UX |
| **Integrante 6** | `@usuario6` | email6@exemplo.com | 👥 UX Researcher |
| **Integrante 7** | `@usuario7` | email7@exemplo.com | 📚 Documentador / QA |

---

## 🔧 **Configurações de Desenvolvimento**

### 🐍 **Python & Ambientes Virtuais**
```bash
# Versão recomendada
Python 3.8+

# Para Django
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements-django.txt

# Para Flask  
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 🗃️ **Banco de Dados - Configurações**

#### **Desenvolvimento (SQLite):**
```env
# Arquivo .env (criar na raiz do projeto)
SECRET_KEY=sua-chave-secreta-aqui-123456
DEBUG=True
USE_SQLITE=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### **Produção (MySQL) - Para usar futuramente:**
```env
SECRET_KEY=chave-super-secreta-producao
DEBUG=False
DB_NAME=carteira_pet
DB_USER=root
DB_PASSWORD=senha_mysql
DB_HOST=localhost
DB_PORT=3306
ALLOWED_HOSTS=seu-dominio.com,localhost
```

### 🚀 **URLs de Desenvolvimento**

#### **Django (Opção Principal):**
- **Servidor local:** http://127.0.0.1:8000
- **Admin Django:** http://127.0.0.1:8000/admin
- **API Status:** http://127.0.0.1:8000/api/status

#### **Flask (Opção Alternativa):**
- **Servidor local:** http://127.0.0.1:5000
- **Hello World:** http://127.0.0.1:5000/hello
- **API Status:** http://127.0.0.1:5000/api/status
- **Sobre:** http://127.0.0.1:5000/sobre

---

## 🔐 **Credenciais de Acesso**

### **Django Admin (criar após setup):**
```bash
# Comando para criar superusuário:
cd django_app
python manage.py createsuperuser

# Usuário sugerido para desenvolvimento:
Username: admin
Email: admin@carteirapet.com
Password: [definir uma senha segura]
```

### **MySQL (se usar em produção):**
```sql
-- Banco de dados
Database: carteira_pet
Username: carteira_user
Password: [definir senha segura]

-- Comando para criar:
CREATE DATABASE carteira_pet CHARACTER SET utf8mb4;
CREATE USER 'carteira_user'@'localhost' IDENTIFIED BY 'senha_segura';
GRANT ALL PRIVILEGES ON carteira_pet.* TO 'carteira_user'@'localhost';
```

---

## 📱 **Comunicação da Equipe**

### 💬 **Canais de Comunicação**
- **WhatsApp/Telegram:** [Link do grupo - adicionar]
- **Discord:** [Link do servidor - adicionar]
- **Email:** equipe-carteira-pet@univesp.edu.br (exemplo)
- **Reuniões:** [Definir horário e plataforma]

### 📅 **Cronograma de Reuniões**
| Tipo | Frequência | Horário | Plataforma |
|------|------------|---------|------------|
| **Stand-up** | Diário | [Definir] | WhatsApp/Discord |
| **Sprint Review** | Semanal | [Definir] | Zoom/Meet |
| **Planning** | Quinzenal | [Definir] | Presencial/Online |

---

## 🛠️ **Ferramentas e Acessos**

### 🔧 **Desenvolvimento**
- **IDE:** VS Code (recomendado)
- **Git Client:** GitHub Desktop ou Git CLI
- **Database:** MySQL Workbench (se usar MySQL)
- **API Testing:** Postman
- **Design:** Figma (para wireframes)

### 🌐 **Deploy e Produção (Futuro)**
- **Servidor:** [A definir - Heroku, DigitalOcean, etc.]
- **Domínio:** [A definir]
- **SSL:** [A configurar]
- **Monitoramento:** [A definir]

---

## 📝 **Padrões e Convenções**

### 🌿 **Git Workflow**
```bash
# Convenção de branches:
main                    # Branch principal
feature/nome-da-feature # Novas funcionalidades  
fix/nome-do-bug        # Correções
docs/atualizacao       # Documentação

# Convenção de commits:
feat: adiciona nova funcionalidade
fix: corrige bug específico
docs: atualiza documentação
style: formatação de código
refactor: refatoração sem mudança funcional
test: adiciona ou corrige testes
```

### 📋 **Code Review**
- **Mínimo:** 1 aprovação para merge
- **Responsável final:** Integrante 2 (Tech Lead)
- **Checklist:** Funcionalidade, testes, documentação

---

## 🔒 **Segurança e Backup**

### 🛡️ **Boas Práticas**
- ❌ **NUNCA commitar** senhas ou chaves no código
- ✅ **Sempre usar** arquivo `.env` para configurações
- ✅ **Fazer backup** do banco de dados semanalmente
- ✅ **Manter dependências** atualizadas

### 📊 **Monitoramento**
- **Logs:** Verificar diariamente durante desenvolvimento
- **Performance:** Monitorar tempo de resposta
- **Errors:** Rastrear e corrigir rapidamente
- **Usage:** Acompanhar métricas de uso

---

## 📞 **Contatos de Emergência**

### 👨‍🏫 **Orientação Acadêmica**
- **Professor Orientador:** Prof. [Nome] - email@univesp.edu.br
- **Coordenação:** [Contato da coordenação]
- **Suporte Técnico UNIVESP:** [Contato de suporte]

### 🆘 **Suporte Técnico**
- **GitHub Issues:** Para problemas do repositório
- **Documentação:** README.md e GUIA_DE_UTILIZACAO.md
- **Stack Overflow:** Para dúvidas técnicas específicas
- **Django Docs:** https://docs.djangoproject.com/
- **Flask Docs:** https://flask.palletsprojects.com/

---

## 📈 **Métricas e Objetivos**

### 🎯 **Metas por Quinzena**
- **Q1-2:** Estrutura e planejamento ✅
- **Q3-4:** MVP funcionando
- **Q5-8:** Funcionalidades completas
- **Q9-12:** Refinamentos e testes
- **Q13-14:** Deploy e apresentação

### 📊 **KPIs do Projeto**
- **Commits:** Mínimo 2-3 por semana por integrante
- **Tests:** Cobertura mínima de 70%
- **Documentation:** Todas as funcionalidades documentadas
- **Performance:** Tempo de resposta < 2s

---

## 🔄 **Processo de Atualização**

### 📝 **Como atualizar este documento:**
1. Fazer alterações necessárias
2. Commit com mensagem: `docs: atualiza credenciais da equipe`
3. Notificar equipe sobre mudanças
4. Manter versão atualizada para novos integrantes

### 🕒 **Última atualização:** 29/03/2026
### 👤 **Responsável pela manutenção:** Integrante 1 (Líder)

---

> **⚠️ IMPORTANTE:** Este arquivo contém informações sensíveis. Mantenha-o seguro e atualizado. Não compartilhe credenciais fora da equipe do projeto.

> **📝 NOTA:** Substitua todas as informações entre `[colchetes]` pelas informações reais da sua equipe.

**Desenvolvido para PJI110 - UNIVESP 2026**

**Co-Authored-By: Oz <oz-agent@warp.dev>**