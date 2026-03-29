# ANÁLISE DE REQUISITOS DO SISTEMA
## Carteira Digital de Vacinação para PET

**Disciplina:** PJI110 - Projeto Integrador em Computação I  
**Instituição:** UNIVESP - Universidade Virtual do Estado de São Paulo  
**Data:** Março de 2026  
**Equipe:** 7 Integrantes

---

## IDENTIFICAÇÃO DA EQUIPE

| # | Nome | Papel | Responsabilidade Principal |
|---|------|-------|----------------------------|
| 1 | [Nome Integrante 1] | Líder do Projeto / Product Owner | Coordenação geral, entregas, comunicação com professor |
| 2 | [Nome Integrante 2] | Arquiteto de Software / Tech Lead | Arquitetura do sistema, padrões técnicos, Git |
| 3 | [Nome Integrante 3] | Desenvolvedor Backend | Rotas Flask, lógica de negócio, APIs |
| 4 | [Nome Integrante 4] | Especialista em Banco de Dados | Modelagem, ORM, migrations, queries |
| 5 | [Nome Integrante 5] | Desenvolvedor Frontend / UI/UX | Interface, templates, Bootstrap, responsividade |
| 6 | [Nome Integrante 6] | Analista de Requisitos / UX Researcher | Entrevistas, personas, casos de uso, validação |
| 7 | [Nome Integrante 7] | Documentador / QA | Documentação técnica, testes, referências |

---

## 1. INTRODUÇÃO

### 1.1 Propósito do Documento
Este documento apresenta a análise de requisitos do sistema **Carteira Digital de Vacinação para PET**, elaborado pela equipe de 7 integrantes. Detalha as funcionalidades, características técnicas, restrições e a divisão de responsabilidades no desenvolvimento do projeto.

**Responsável pela elaboração:** Integrante 6 (Analista de Requisitos)  
**Revisores técnicos:** Integrante 2 (Arquiteto) e Integrante 4 (BD)  
**Consolidação final:** Integrante 7 (Documentador)

### 1.2 Escopo do Projeto
O sistema proposto é uma aplicação web que permite aos donos de animais de estimação (pets) gerenciar de forma digital o histórico completo de vacinação e saúde de seus animais, substituindo as tradicionais carteirinhas de papel.

**Metodologia de desenvolvimento:** Design Thinking (5 fases) + Desenvolvimento Ágil  
**Coordenação:** Integrante 1 (Líder)

### 1.3 Definições e Abreviações
- **Pet:** Animal de estimação
- **Tutor:** Dono/responsável pelo pet
- **MVP:** Minimum Viable Product (Produto Mínimo Viável)
- **CRUD:** Create, Read, Update, Delete (Criar, Ler, Atualizar, Deletar)
- **ORM:** Object-Relational Mapping
- **ER:** Entidade-Relacionamento

---

## 2. DESCRIÇÃO GERAL DO SISTEMA

### 2.1 Perspectiva do Produto
A Carteira Digital de Vacinação para PET é um sistema web independente que visa modernizar o controle de saúde animal, oferecendo uma alternativa digital, segura e acessível às carteiras de vacinação físicas.

**Proposta de valor identificada:** 
- Através de 7-10 entrevistas realizadas (Integrante 6)
- Análise de mercado (Integrante 6 + Integrante 5)
- Validação técnica de viabilidade (Integrante 2 + Integrante 3 + Integrante 4)

### 2.2 Funções do Produto
O sistema permitirá:
- Cadastro e autenticação de tutores **(Implementação: Integrante 3)**
- Gerenciamento de múltiplos pets por tutor **(Implementação: Integrante 3 + Integrante 4)**
- Registro completo do histórico de vacinação **(Implementação: Integrante 3 + Integrante 4)**
- Visualização organizada dos dados de saúde **(Design: Integrante 5, Implementação: Integrante 3)**
- Alertas automáticos sobre vacinas próximas do vencimento **(Implementação: Integrante 3)**
- Acesso multiplataforma - computador, tablet, celular **(Responsividade: Integrante 5)**

### 2.3 Características dos Usuários

| Tipo de Usuário | Descrição | Conhecimento Técnico | Persona Desenvolvida Por |
|-----------------|-----------|---------------------|--------------------------|
| Tutor de Pet | Pessoa física, dono de animal de estimação | Básico (uso de internet) | Integrante 6 + Integrante 5 |
| Administrador | Responsável pela manutenção do sistema | Avançado (técnico) | Integrante 2 |

**Personas detalhadas:** Ver documento `docs/design_thinking/Fase1_Empatia.md` (Integrante 6)

### 2.4 Restrições
- Sistema web (requer conexão com internet)
- Desenvolvido com tecnologias gratuitas e open-source
- Prazo de desenvolvimento: 14 semanas
- Interface em português brasileiro
- Compatível com navegadores modernos (Chrome, Firefox, Edge)
- **Equipe:** 7 integrantes, ~18-20h/pessoa/quinzena

---

## 3. REQUISITOS FUNCIONAIS

### 3.1 Módulo de Autenticação
**Responsável pela implementação:** Integrante 3 (Backend)  
**Validação de segurança:** Integrante 2 (Arquiteto)

**RF01 - Cadastro de Usuário**
- **Descrição:** O sistema deve permitir que novos tutores criem uma conta
- **Entrada:** Nome completo, e-mail, senha, confirmação de senha
- **Processo:** Validação de dados, verificação de e-mail único, criptografia de senha
- **Saída:** Conta criada com sucesso ou mensagem de erro
- **Prioridade:** Alta (MVP)
- **Levantado por:** Integrante 6 (entrevistas com usuários)

**RF02 - Login de Usuário**
- **Descrição:** O sistema deve autenticar tutores cadastrados
- **Entrada:** E-mail e senha
- **Processo:** Verificação de credenciais no banco de dados
- **Saída:** Acesso ao sistema ou mensagem de erro
- **Prioridade:** Alta (MVP)
- **Tecnologia:** Flask-Login (definido por Integrante 2)

**RF03 - Logout**
- **Descrição:** O sistema deve permitir que o usuário encerre sua sessão
- **Entrada:** Comando de logout
- **Processo:** Encerrar sessão ativa
- **Saída:** Retorno à tela de login
- **Prioridade:** Alta (MVP)

**RF04 - Recuperação de Senha**
- **Descrição:** O sistema deve permitir recuperação de senha via e-mail
- **Entrada:** E-mail cadastrado
- **Processo:** Envio de link de redefinição
- **Saída:** E-mail enviado ou mensagem de erro
- **Prioridade:** Média

### 3.2 Módulo de Gerenciamento de Pets
**Responsável pela implementação:** Integrante 3 (Backend)  
**Modelagem BD:** Integrante 4  
**Interface:** Integrante 5 (Frontend)

**RF05 - Cadastrar Pet**
- **Descrição:** O tutor pode adicionar um novo pet ao sistema
- **Entrada:** 
  - Nome do pet (obrigatório)
  - Espécie (cão, gato, outros)
  - Raça
  - Data de nascimento
  - Sexo
  - Peso
  - Cor
  - Foto (opcional - upload Integrante 3)
- **Processo:** Validação e armazenamento dos dados
- **Saída:** Pet cadastrado com sucesso
- **Prioridade:** Alta (MVP)
- **Wireframe:** Criado por Integrante 5

**RF06 - Listar Pets**
- **Descrição:** O tutor visualiza todos os seus pets cadastrados
- **Entrada:** Usuário autenticado
- **Processo:** Buscar pets do usuário no banco de dados
- **Saída:** Lista com cards/resumo de cada pet
- **Prioridade:** Alta (MVP)
- **Design de cards:** Integrante 5 (Bootstrap)

**RF07 - Visualizar Detalhes do Pet**
- **Descrição:** Exibir informações completas de um pet específico
- **Entrada:** Seleção de um pet
- **Processo:** Buscar dados completos do pet
- **Saída:** Página com todos os dados e histórico
- **Prioridade:** Alta (MVP)

**RF08 - Editar Pet**
- **Descrição:** O tutor pode atualizar informações do pet
- **Entrada:** Novos dados do pet
- **Processo:** Validação e atualização no banco
- **Saída:** Dados atualizados com sucesso
- **Prioridade:** Média

**RF09 - Excluir Pet**
- **Descrição:** O tutor pode remover um pet do sistema
- **Entrada:** Confirmação de exclusão
- **Processo:** Remoção do pet e dados relacionados (cascade - Integrante 4)
- **Saída:** Pet excluído com sucesso
- **Prioridade:** Média

### 3.3 Módulo de Vacinação
**Responsável:** Integrante 3 (Backend) + Integrante 4 (relacionamentos BD)

**RF10 - Registrar Vacina**
- **Descrição:** Adicionar novo registro de vacina aplicada
- **Entrada:**
  - Nome da vacina (obrigatório)
  - Data de aplicação (obrigatório)
  - Veterinário responsável
  - Clínica veterinária
  - Lote da vacina
  - Data da próxima dose
  - Observações
- **Processo:** Validação e armazenamento
- **Saída:** Vacina registrada com sucesso
- **Prioridade:** Alta (MVP)
- **Validação de negócio:** Definida por Integrante 6

**RF11 - Visualizar Histórico de Vacinas**
- **Descrição:** Exibir todas as vacinas do pet em ordem cronológica
- **Entrada:** Pet selecionado
- **Processo:** Buscar vacinas do pet no banco (query otimizada - Integrante 4)
- **Saída:** Lista ordenada por data
- **Prioridade:** Alta (MVP)
- **Design timeline:** Integrante 5

**RF12 - Editar Registro de Vacina**
- **Descrição:** Atualizar informações de uma vacina
- **Entrada:** Novos dados da vacina
- **Processo:** Validação e atualização
- **Saída:** Vacina atualizada
- **Prioridade:** Média

**RF13 - Excluir Registro de Vacina**
- **Descrição:** Remover registro de vacina
- **Entrada:** Confirmação de exclusão
- **Processo:** Remoção do banco de dados
- **Saída:** Vacina excluída
- **Prioridade:** Baixa

**RF14 - Filtrar Vacinas**
- **Descrição:** Buscar vacinas por critérios específicos
- **Entrada:** Filtros (período, nome da vacina, etc.)
- **Processo:** Busca filtrada no banco
- **Saída:** Lista de vacinas filtradas
- **Prioridade:** Média

### 3.4 Módulo de Alertas
**Responsável:** Integrante 3 (lógica) + Integrante 5 (visualização)

**RF15 - Alertas de Vacinas Próximas**
- **Descrição:** Notificar sobre vacinas com vencimento próximo
- **Entrada:** Sistema verifica datas automaticamente
- **Processo:** Comparar data atual com próximas doses (cron job ou verificação on-demand)
- **Saída:** Avisos na dashboard e/ou por e-mail
- **Prioridade:** Média
- **Algoritmo:** Desenvolvido por Integrante 3

**RF16 - Dashboard com Resumo**
- **Descrição:** Página inicial com visão geral
- **Entrada:** Usuário autenticado
- **Processo:** Consolidar informações dos pets
- **Saída:** 
  - Número total de pets
  - Vacinas em dia / atrasadas
  - Próximas vacinas
  - Pets cadastrados recentemente
- **Prioridade:** Média
- **Design:** Integrante 5 (cards com Bootstrap)
- **Wireframe:** Integrante 5

### 3.5 Funcionalidades Adicionais (Opcionais)
**Responsável pela priorização:** Integrante 1 (Líder) com input da equipe

**RF17 - Upload de Documentos**
- **Descrição:** Anexar exames e documentos veterinários
- **Prioridade:** Baixa (extra se der tempo)
- **Implementação:** Integrante 3

**RF18 - Gerar Carteirinha em PDF**
- **Descrição:** Exportar carteirinha de vacinação em PDF
- **Prioridade:** Baixa (extra)
- **Implementação:** Integrante 3 (backend) + Integrante 5 (template)

**RF19 - Compartilhar Carteirinha**
- **Descrição:** Gerar link público para visualização
- **Prioridade:** Baixa (extra)

---

## 4. REQUISITOS NÃO-FUNCIONAIS

### 4.1 Requisitos de Usabilidade
**Responsável:** Integrante 5 (Frontend) + Integrante 6 (validação UX)

**RNF01 - Interface Intuitiva**
- O sistema deve ter navegação clara e autoexplicativa
- Máximo de 3 cliques para acessar qualquer funcionalidade principal
- **Validação:** Testes de usabilidade com 3-5 usuários (Integrante 6)

**RNF02 - Responsividade**
- Interface deve se adaptar a diferentes tamanhos de tela
- Compatível com dispositivos móveis (smartphones e tablets)
- **Implementação:** Mobile-first approach (Integrante 5 - Bootstrap)
- **Testes:** Chrome DevTools + dispositivos reais

**RNF03 - Feedback Visual**
- Todas as ações devem ter confirmação visual clara
- Mensagens de erro devem ser descritivas e úteis
- **Implementação:** Alerts do Bootstrap + validação de formulários (Integrante 5)

### 4.2 Requisitos de Desempenho
**Responsável:** Integrante 2 (Arquiteto) + Integrante 4 (otimização BD)

**RNF04 - Tempo de Resposta**
- Páginas principais devem carregar em até 3 segundos
- Operações no banco devem responder em até 1 segundo
- **Monitoramento:** A definir (logs básicos)

**RNF05 - Capacidade**
- Sistema deve suportar pelo menos 100 usuários simultâneos
- Cada usuário pode ter até 20 pets cadastrados
- **Validação:** Testes de carga (opcional)

### 4.3 Requisitos de Segurança
**Responsável:** Integrante 2 (Arquiteto) + Integrante 3 (implementação)

**RNF06 - Autenticação**
- Senhas devem ser armazenadas com hash (bcrypt ou similar)
- Sessões devem expirar após 24h de inatividade
- **Biblioteca:** Werkzeug Security (Flask padrão)

**RNF07 - Autorização**
- Usuários só podem acessar dados dos próprios pets
- Proteção contra SQL Injection (uso de ORM - Integrante 4)
- Proteção contra XSS (escape de templates Jinja2)

**RNF08 - Privacidade**
- Dados pessoais devem seguir boas práticas de privacidade
- Opção de exclusão completa da conta
- **Conformidade:** LGPD básica (documentado por Integrante 7)

### 4.4 Requisitos de Confiabilidade
**Responsável:** Integrante 2 (estratégia) + Integrante 7 (documentação)

**RNF09 - Disponibilidade**
- Sistema deve estar disponível 95% do tempo (em produção)
- Backup automático do banco de dados
- **Estratégia de backup:** A definir na fase de deploy

**RNF10 - Recuperação de Erros**
- Mensagens de erro claras sem expor informações técnicas
- Log de erros para depuração
- **Implementação:** Python logging module (Integrante 3)

### 4.5 Requisitos de Manutenibilidade
**Responsável:** Toda a equipe (code review por Integrante 2)

**RNF11 - Código Limpo**
- Código comentado e documentado
- Seguir boas práticas de programação (PEP 8 para Python)
- **Ferramentas:** pylint, black (formatação automática)
- **Code review:** Obrigatório via Pull Requests

**RNF12 - Versionamento**
- Código versionado com Git
- Commits descritivos e organizados
- **Convenção:** Conventional Commits (definido por Integrante 2)
- **Workflow:** Git Flow (branches: main, develop, feature/*)

---

## 5. CASOS DE USO

**Responsável pela elaboração:** Integrante 6 (Analista de Requisitos)  
**Validação técnica:** Integrante 3 (Backend)

### UC01: Cadastrar Novo Pet

**Ator Principal:** Tutor do Pet  
**Pré-condições:** Usuário deve estar autenticado  
**Complexidade:** Média

**Fluxo Principal:**
1. Tutor acessa página "Meus Pets"
2. Tutor clica em "Adicionar Novo Pet"
3. Sistema exibe formulário de cadastro (design: Integrante 5)
4. Tutor preenche dados obrigatórios (nome, espécie)
5. Tutor opcionalmente adiciona foto (upload: Integrante 3)
6. Tutor clica em "Salvar"
7. Sistema valida dados (backend: Integrante 3)
8. Sistema armazena pet no banco de dados (Integrante 4)
9. Sistema exibe mensagem de sucesso
10. Sistema redireciona para lista de pets

**Fluxos Alternativos:**
- **7a.** Dados inválidos ou incompletos:
  - Sistema exibe mensagens de erro (implementação: Integrante 5)
  - Usuário corrige dados e tenta novamente

**Pós-condições:** Novo pet cadastrado e visível na lista

**Wireframe:** Ver `docs/wireframes/cadastro_pet.png` (Integrante 5)

---

### UC02: Registrar Vacinação

**Ator Principal:** Tutor do Pet  
**Pré-condições:** 
- Usuário autenticado
- Pelo menos um pet cadastrado

**Fluxo Principal:**
1. Tutor seleciona um pet
2. Tutor acessa "Histórico de Vacinas"
3. Tutor clica em "Adicionar Vacina"
4. Sistema exibe formulário (template: Integrante 5)
5. Tutor preenche dados da vacina
6. Tutor define data da próxima dose (se aplicável)
7. Tutor clica em "Salvar"
8. Sistema valida dados (Integrante 3)
9. Sistema armazena vacina (Integrante 4 - relacionamento Pet-Vacina)
10. Sistema atualiza histórico
11. Sistema cria alerta para próxima dose se informada (Integrante 3)

**Fluxos Alternativos:**
- **8a.** Data futura inválida:
  - Sistema impede data de aplicação futura (regra de negócio)
  - Exibe mensagem de erro

**Pós-condições:** Vacina registrada e visível no histórico

**Regra de Negócio Relacionada:** RN04 (definida por Integrante 6)

---

### UC03: Consultar Vacinas Pendentes

**Ator Principal:** Tutor do Pet  
**Pré-condições:** Usuário autenticado

**Fluxo Principal:**
1. Tutor acessa dashboard
2. Sistema busca vacinas com próxima dose agendada (query: Integrante 4)
3. Sistema compara com data atual (lógica: Integrante 3)
4. Sistema exibe lista de vacinas pendentes/próximas
5. Sistema destaca vacinas atrasadas em vermelho (CSS: Integrante 5)
6. Tutor pode clicar em uma vacina para ver detalhes

**Pós-condições:** Tutor informado sobre status das vacinas

**Dashboard Design:** Integrante 5

---

## 6. MODELO DE DADOS

**Responsável:** Integrante 4 (Especialista em Banco de Dados)  
**Revisão:** Integrante 2 (Arquiteto)

### 6.1 Diagrama Entidade-Relacionamento (Conceitual)

```
┌─────────────────┐
│    USUARIO      │
├─────────────────┤
│ id (PK)         │
│ nome            │
│ email (unique)  │
│ senha_hash      │
│ data_cadastro   │
└────────┬────────┘
         │
         │ 1:N (Um usuário pode ter vários pets)
         │
┌────────▼────────┐
│      PET        │
├─────────────────┤
│ id (PK)         │
│ usuario_id (FK) │
│ nome            │
│ especie         │
│ raca            │
│ data_nascimento │
│ sexo            │
│ peso            │
│ cor             │
│ foto_path       │
│ data_cadastro   │
└────────┬────────┘
         │
         │ 1:N (Um pet pode ter várias vacinas)
         │
┌────────▼────────┐
│     VACINA      │
├─────────────────┤
│ id (PK)         │
│ pet_id (FK)     │
│ nome_vacina     │
│ data_aplicacao  │
│ veterinario     │
│ clinica         │
│ lote            │
│ proxima_dose    │
│ observacoes     │
│ data_registro   │
└─────────────────┘
```

**Normalização aplicada:** 3ª Forma Normal (3FN)  
**Justificativa:** Evitar redundância, manter integridade referencial

### 6.2 Dicionário de Dados

**Elaborado por:** Integrante 4  
**Formato:** Completo, com restrições e descrições

**Tabela: usuarios**

| Campo | Tipo | Tamanho | Restrições | Descrição | Implementação |
|-------|------|---------|------------|-----------|---------------|
| id | INTEGER | - | PK, AUTO_INCREMENT | Identificador único | SQLAlchemy autoincrement |
| nome | VARCHAR | 100 | NOT NULL | Nome completo do tutor | - |
| email | VARCHAR | 120 | NOT NULL, UNIQUE | E-mail para login | Index criado |
| senha_hash | VARCHAR | 255 | NOT NULL | Senha criptografada | bcrypt hash |
| data_cadastro | DATETIME | - | NOT NULL, DEFAULT NOW | Data de registro | Timestamp automático |

**Tabela: pets**

| Campo | Tipo | Tamanho | Restrições | Descrição | Implementação |
|-------|------|---------|------------|-----------|---------------|
| id | INTEGER | - | PK, AUTO_INCREMENT | Identificador único | - |
| usuario_id | INTEGER | - | FK, NOT NULL | Dono do pet | ON DELETE CASCADE |
| nome | VARCHAR | 50 | NOT NULL | Nome do pet | - |
| especie | VARCHAR | 30 | NOT NULL | Cão, gato, etc. | - |
| raca | VARCHAR | 50 | NULL | Raça do animal | Opcional |
| data_nascimento | DATE | - | NULL | Data de nascimento | Validação <= hoje |
| sexo | VARCHAR | 10 | NULL | Macho/Fêmea | - |
| peso | DECIMAL | 5,2 | NULL | Peso em kg | - |
| cor | VARCHAR | 30 | NULL | Cor predominante | - |
| foto_path | VARCHAR | 255 | NULL | Caminho da foto | Upload handler |
| data_cadastro | DATETIME | - | NOT NULL, DEFAULT NOW | Data de cadastro | - |

**Tabela: vacinas**

| Campo | Tipo | Tamanho | Restrições | Descrição | Implementação |
|-------|------|---------|------------|-----------|---------------|
| id | INTEGER | - | PK, AUTO_INCREMENT | Identificador único | - |
| pet_id | INTEGER | - | FK, NOT NULL | Pet vacinado | ON DELETE CASCADE |
| nome_vacina | VARCHAR | 100 | NOT NULL | Nome da vacina | - |
| data_aplicacao | DATE | - | NOT NULL | Quando foi aplicada | Validação <= hoje |
| veterinario | VARCHAR | 100 | NULL | Nome do veterinário | - |
| clinica | VARCHAR | 100 | NULL | Nome da clínica | - |
| lote | VARCHAR | 50 | NULL | Lote da vacina | - |
| proxima_dose | DATE | - | NULL | Data da próxima dose | Usado para alertas |
| observacoes | TEXT | - | NULL | Informações adicionais | - |
| data_registro | DATETIME | - | NOT NULL, DEFAULT NOW | Quando foi registrado | - |

**Índices criados:**
- `idx_usuario_email` em `usuarios.email` (busca rápida no login)
- `idx_pet_usuario` em `pets.usuario_id` (listar pets por usuário)
- `idx_vacina_pet` em `vacinas.pet_id` (histórico de vacinas)
- `idx_vacina_proxima_dose` em `vacinas.proxima_dose` (alertas)

**Migrations:** Gerenciadas por Flask-Migrate (Integrante 4)

---

## 7. ARQUITETURA DO SISTEMA

**Responsável:** Integrante 2 (Arquiteto de Software)  
**Validação técnica:** Equipe técnica (Integrantes 2, 3, 4)

### 7.1 Arquitetura de Alto Nível

```
┌─────────────────────────────────────────┐
│         CAMADA DE APRESENTAÇÃO          │
│  (HTML, CSS, Bootstrap, JavaScript)     │
│                                         │
│  Responsável: Integrante 5 (Frontend)  │
└──────────────────┬──────────────────────┘
                   │ HTTP Requests/Responses
┌──────────────────▼──────────────────────┐
│        CAMADA DE APLICAÇÃO              │
│     (Flask - Framework Web Python)      │
│  - Routes (URLs)                        │
│  - Controllers (Lógica)                 │
│  - Forms (Validações)                   │
│                                         │
│  Responsável: Integrante 3 (Backend)   │
└──────────────────┬──────────────────────┘
                   │ ORM Calls
┌──────────────────▼──────────────────────┐
│        CAMADA DE NEGÓCIO                │
│     (Models - SQLAlchemy ORM)           │
│  - Usuario                              │
│  - Pet                                  │
│  - Vacina                               │
│                                         │
│  Responsável: Integrante 4 (BD)        │
└──────────────────┬──────────────────────┘
                   │ SQL Queries
┌──────────────────▼──────────────────────┐
│        CAMADA DE DADOS                  │
│    (SQLite / PostgreSQL)                │
│                                         │
│  Responsável: Integrante 4 (BD)        │
└─────────────────────────────────────────┘
```

### 7.2 Tecnologias Utilizadas

**Backend:**
- Python 3.8+ *(decisão: Integrante 2)*
- Flask 3.0 (Framework web) *(escolha consensual)*
- Flask-SQLAlchemy (ORM - banco de dados) *(Integrante 4)*
- Flask-Login (Autenticação) *(Integrante 3)*
- Flask-WTF (Formulários e validação) *(Integrante 3)*
- Werkzeug (Segurança - hash de senhas) *(Integrante 2)*
- Flask-Migrate (Migrations) *(Integrante 4)*

**Frontend:**
- HTML5 *(Integrante 5)*
- CSS3 *(Integrante 5)*
- Bootstrap 5 (Framework CSS responsivo) *(escolha: Integrante 5)*
- JavaScript (interações básicas) *(Integrante 5)*

**Banco de Dados:**
- SQLite (Desenvolvimento) *(Integrante 4)*
- PostgreSQL (Produção - opcional) *(Integrante 4)*

**Controle de Versão:**
- Git *(Integrante 2 - Git Flow)*
- GitHub *(repositório gerenciado por Integrante 2)*

**Ferramentas de Desenvolvimento:**
- Visual Studio Code *(todos os integrantes)*
- Git Bash / PowerShell *(todos)*
- DB Browser for SQLite *(visualizar banco - Integrante 4)*
- Figma *(wireframes - Integrante 5)*
- Postman *(testar APIs - Integrante 7)*

**Justificativa das escolhas técnicas:** Ver documento `docs/decisoes_tecnicas.md` *(Integrante 2 + Integrante 7)*

---

## 8. INTERFACE DO USUÁRIO (WIREFRAMES)

**Responsável:** Integrante 5 (Desenvolvedor Frontend / UI/UX)  
**Validação com usuários:** Integrante 6 (UX Researcher)

**Ferramentas utilizadas:** Figma (alta fidelidade), ASCII (documentação)

### 8.1 Tela de Login

```
┌─────────────────────────────────────────┐
│                                         │
│         🐾 CARTEIRA PET 🐾             │
│                                         │
│    ┌─────────────────────────────┐    │
│    │ Email                       │    │
│    │ ___________________________│    │
│    │                             │    │
│    │ Senha                       │    │
│    │ ___________________________│    │
│    │                             │    │
│    │  [ Entrar ]                 │    │
│    │                             │    │
│    │  Esqueceu a senha?          │    │
│    │  Não tem conta? Cadastre-se │    │
│    └─────────────────────────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

**Arquivo Figma:** `docs/wireframes/login.fig` *(Integrante 5)*  
**Paleta de cores:** Verde (#28a745), Azul (#007bff), Branco (#fff) *(Integrante 5)*

### 8.2 Dashboard Principal

```
┌─────────────────────────────────────────┐
│ [Logo] Carteira Pet    [Meus Pets] [Sair]│
├─────────────────────────────────────────┤
│                                         │
│  Olá, Maria! 👋                        │
│                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐│
│  │ 🐕 3     │ │ ⚠️ 2     │ │ ✅ 5     ││
│  │ Pets     │ │ Vacinas  │ │ Em dia   ││
│  │          │ │ Próximas │ │          ││
│  └──────────┘ └──────────┘ └──────────┘│
│                                         │
│  📋 Vacinas Próximas:                  │
│  ┌─────────────────────────────────┐  │
│  │ • Rex - V10 (Polivalente)       │  │
│  │   Vence em: 3 dias              │  │
│  ├─────────────────────────────────┤  │
│  │ • Luna - Antirrábica            │  │
│  │   Vence em: 10 dias             │  │
│  └─────────────────────────────────┘  │
│                                         │
│  [+ Adicionar Pet]                     │
│                                         │
└─────────────────────────────────────────┘
```

**Componentes Bootstrap:** Cards, Badges, Alerts *(Integrante 5)*  
**Lógica de alertas:** Implementada por Integrante 3

### 8.3 Lista de Pets

```
┌─────────────────────────────────────────┐
│ [Logo] Carteira Pet    [Dashboard] [Sair]│
├─────────────────────────────────────────┤
│                                         │
│  Meus Pets                 [+ Novo Pet] │
│                                         │
│  ┌─────────────────────────────────┐  │
│  │ [Foto] Rex                      │  │
│  │        Cão - Labrador           │  │
│  │        2 anos - Macho           │  │
│  │        [Ver Detalhes] [Editar]  │  │
│  └─────────────────────────────────┘  │
│                                         │
│  ┌─────────────────────────────────┐  │
│  │ [Foto] Luna                     │  │
│  │        Gato - Persa             │  │
│  │        1 ano - Fêmea            │  │
│  │        [Ver Detalhes] [Editar]  │  │
│  └─────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

**Grid responsivo:** col-md-6 col-lg-4 (2 cols tablet, 3 cols desktop) *(Integrante 5)*

### 8.4 Histórico de Vacinas

```
┌─────────────────────────────────────────┐
│ [← Voltar] Rex - Histórico de Vacinas  │
├─────────────────────────────────────────┤
│                                         │
│  [+ Adicionar Vacina]                  │
│                                         │
│  ┌─────────────────────────────────┐  │
│  │ ✅ V10 (Polivalente)            │  │
│  │    15/02/2026                   │  │
│  │    Dr. João Silva               │  │
│  │    Próxima: 15/03/2026          │  │
│  │    [Detalhes] [Editar]          │  │
│  └─────────────────────────────────┘  │
│                                         │
│  ┌─────────────────────────────────┐  │
│  │ ✅ Antirrábica                  │  │
│  │    10/01/2026                   │  │
│  │    Dra. Ana Costa               │  │
│  │    Próxima: 10/01/2027          │  │
│  │    [Detalhes] [Editar]          │  │
│  └─────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

**Timeline design:** Lista ordenada com badges coloridos *(Integrante 5)*  
**Ordenação:** Query ORDER BY data_aplicacao DESC *(Integrante 4)*

**Total de wireframes criados:** 8 telas principais *(Integrante 5)*  
**Arquivo completo:** `docs/wireframes/` *(pasta no repositório)*

---

## 9. REGRAS DE NEGÓCIO

**Levantadas por:** Integrante 6 (Analista de Requisitos)  
**Validadas com:** Entrevistas com 7-10 usuários (tutores de pets)  
**Implementação:** Integrante 3 (Backend) + Integrante 4 (constraints BD)

**RN01:** Um usuário só pode visualizar e gerenciar seus próprios pets  
*Implementação: Autorização em routes (Flask-Login current_user)*

**RN02:** Um pet pode ter apenas um dono (usuário)  
*Implementação: Relacionamento 1:N no modelo*

**RN03:** Um pet pode ter múltiplas vacinas registradas  
*Implementação: Relacionamento 1:N (Pet -> Vacina)*

**RN04:** Data de aplicação de vacina não pode ser futura  
*Implementação: Validação no form (Flask-WTF) e no backend*

**RN05:** Email de usuário deve ser único no sistema  
*Implementação: UNIQUE constraint no BD + validação no cadastro*

**RN06:** Senha deve ter no mínimo 8 caracteres (atualizado de 6)  
*Implementação: Flask-WTF validators.Length(min=8)*

**RN07:** Nome do pet é obrigatório  
*Implementação: NOT NULL no BD + validação form*

**RN08:** Espécie do pet é obrigatória  
*Implementação: NOT NULL no BD + validação form*

**RN09:** Ao excluir um pet, todas as vacinas relacionadas são excluídas (cascade)  
*Implementação: ON DELETE CASCADE no FK*

**RN10:** Ao excluir um usuário, todos os pets e vacinas relacionados são excluídos  
*Implementação: Cascade em cadeia (Usuario -> Pet -> Vacina)*

**RN11:** Alertas são gerados para vacinas com próxima dose em até 30 dias (atualizado)  
*Implementação: Query WHERE proxima_dose <= CURRENT_DATE + 30*  
*Decisão da equipe: 30 dias (não 15) após feedback de entrevistas*

**RN12:** Fotos de pets devem ter tamanho máximo de 5MB  
*Implementação: Validação no upload (Flask)*

**RN13:** Formatos de imagem aceitos: JPG, PNG, GIF  
*Implementação: Extensão de arquivo verificada*

**RN14:** Peso do pet deve ser um valor positivo (nova regra)  
*Implementação: Validação NumberRange(min=0.1)*

**RN15:** Um usuário pode ter no máximo 20 pets cadastrados (nova regra)  
*Implementação: Verificação antes de criar novo pet*  
*Justificativa: Performance e caso de uso realista (validado por Integrante 6)*

---

## 10. CRONOGRAMA DE DESENVOLVIMENTO

**Responsável pela elaboração:** Integrante 1 (Líder) + Integrante 7 (Documentador)  
**Revisado por:** Toda a equipe

| Fase | Semanas | Fase Design Thinking | Atividades | Responsáveis Principais | Entregas |
|------|---------|---------------------|------------|------------------------|----------|
| **Planejamento** | 1-2 | Empatia | Análise de requisitos, entrevistas, setup ambiente, criação repositório, wireframes | Int 1, 2, 5, 6, 7 | Plano de Ação, Análise Requisitos, Wireframes, Repo GitHub |
| **Levantamento** | 3-4 | Definição | Pesquisa bibliográfica, definição tecnologias, modelagem BD, personas | Int 2, 4, 6, 7 | Levantamento Bibliográfico, Personas, Modelo ER final |
| **Desenvolvimento I** | 5-6 | Ideação | Implementação autenticação, CRUD pets, estrutura básica frontend | Int 2, 3, 4, 5 | Protótipo funcional básico (Auth + Pets) |
| **Desenvolvimento II** | 7-8 | Prototipação | Sistema de vacinas, alertas, dashboard, melhorias UI | Int 3, 4, 5 | Sistema completo (MVP) + Relatório Parcial |
| **Testes e Ajustes** | 9-12 | Teste | Testes com usuários, correção bugs, funcionalidades extras, docs | Int 1, 5, 6, 7 | Sistema testado + Feedback usuários |
| **Finalização** | 13-14 | Refinamento | Documentação final, vídeo apresentação, deploy (opcional) | Todos | Relatório Final + Vídeo + Sistema Final |

**Reuniões semanais:** Terças 19h (1h) + Sábados 14h (2h)  
**Ferramenta de gestão:** GitHub Projects (configurado por Integrante 2)  
**Stand-ups assíncronos:** Mensagens diárias no grupo (opcional)

**Milestones principais:**
- **Milestone 1 (Semana 2):** Documentação completa + Repo estruturado
- **Milestone 2 (Semana 6):** MVP Auth + Pets funcionando
- **Milestone 3 (Semana 8):** Sistema completo com Vacinas + Alertas
- **Milestone 4 (Semana 12):** Testes concluídos + Bugs corrigidos
- **Milestone 5 (Semana 14):** Entrega final

---

## 11. RISCOS E MITIGAÇÕES

**Identificados por:** Toda a equipe (workshop de riscos - Semana 1)  
**Monitoramento:** Integrante 1 (Líder) - revisão semanal

| Risco | Probabilidade | Impacto | Mitigação | Responsável |
|-------|---------------|---------|-----------|-------------|
| Falta de experiência com Flask | Alta | Médio | Estudar tutoriais, documentação oficial, workshops internos (Int 3) | Int 2, 3 |
| Problemas com banco de dados | Média | Alto | Usar SQLite (mais simples), backups frequentes, code review | Int 4 |
| Dificuldade com CSS/Design | Média | Baixo | Usar Bootstrap, templates prontos, Integrante 5 lidera | Int 5 |
| Atraso no cronograma | Média | Alto | Priorizar MVP, revisões semanais, redistribuir tarefas se necessário | Int 1 |
| Bugs de segurança | Baixa | Alto | Seguir boas práticas, bibliotecas confiáveis, validação rigorosa, code review | Int 2, 3 |
| Perda de código | Baixa | Alto | Git + GitHub, commits frequentes (mín 2x/semana), backups | Int 2 |
| Conflitos na equipe | Média | Médio | Comunicação clara, reuniões regulares, mediação do líder | Int 1 |
| Ausência de integrante | Média | Médio | Documentação completa, conhecimento distribuído, backup por área | Todos |
| Mudança de requisitos | Baixa | Médio | Validar cedo com usuários, Design Thinking iterativo | Int 6 |

**Plano de contingência geral:**
- Se 1 integrante se ausentar: Redistribuir tarefas entre equipe
- Se atraso crítico: Cortar funcionalidades extras (RF17-RF19)
- Se problema técnico bloqueante: Buscar suporte do professor orientador

---

## 12. DISTRIBUIÇÃO DE RESPONSABILIDADES

### Por Fase do Projeto:

**Quinzena 1-2 (Planejamento):**
- Int 1: Coordenação geral, kick-off, consolidação entregas
- Int 2: Criar repositório, definir arquitetura, Git Flow
- Int 3: Estudar Flask, prototipar Hello World
- Int 4: Modelagem inicial BD, estudar SQLAlchemy
- Int 5: Wireframes, paleta cores, estudar Bootstrap
- Int 6: Entrevistas (7-10), personas, mapa empatia
- Int 7: Levantamento bibliográfico, README, Plano Ação

**Quinzena 3-4 (Levantamento):**
- Int 2: Finalizar decisões técnicas, documentar
- Int 3: Estrutura Flask (blueprints, config)
- Int 4: Models SQLAlchemy, migrations iniciais
- Int 5: Templates base, sistema de componentes
- Int 6: Refinar personas, validar requisitos
- Int 7: Bibliografia completa, formatação ABNT

**Quinzena 5-6 (Desenvolvimento I):**
- Int 3: Sistema de autenticação completo
- Int 3: CRUD de pets (backend)
- Int 4: Relacionamentos BD, queries otimizadas
- Int 5: Templates de auth, CRUD pets (frontend)
- Int 2: Code review, CI básico
- Int 7: Testes manuais, documentar APIs

**Quinzena 7-8 (Desenvolvimento II):**
- Int 3: Sistema de vacinas (backend)
- Int 3: Lógica de alertas
- Int 4: Queries complexas, performance
- Int 5: Dashboard, histórico vacinas (frontend)
- Int 5: Responsividade mobile
- Int 2: Revisão geral, refatorações
- Int 7: Testes integração, docs usuário

**Quinzena 9-12 (Testes):**
- Int 6: Testes de usabilidade (3-5 usuários)
- Int 7: Testes funcionais, relatório bugs
- Int 3: Correção de bugs backend
- Int 5: Correção de bugs frontend
- Int 1: Priorização de correções
- Int 2: Validação técnica final

**Quinzena 13-14 (Finalização):**
- Int 7: Documentação final completa
- Int 5: Vídeo de demonstração
- Int 1: Relatório final, apresentação
- Todos: Revisão geral, aprovação final

### Matriz de Conhecimento (T-Shaped):

| Integrante | Especialidade Principal | Conhecimento Secundário |
|------------|------------------------|------------------------|
| Int 1 | Gestão de Projetos | Visão geral técnica |
| Int 2 | Arquitetura, Git | Python, Flask, Segurança |
| Int 3 | Backend (Flask) | Python, APIs, Lógica |
| Int 4 | Banco de Dados | SQL, ORM, Performance |
| Int 5 | Frontend, UI/UX | HTML/CSS, Bootstrap, Design |
| Int 6 | UX Research | Requisitos, Testes Usabilidade |
| Int 7 | Documentação, QA | Testes, ABNT, Redação Técnica |

---

## 13. CRITÉRIOS DE AVALIAÇÃO DO PROJETO INTEGRADOR

### 13.1. Visão Geral da Avaliação

Este projeto será avaliado conforme as **Orientações Oficiais da UNIVESP para Avaliação do Projeto Integrador (Setembro/2022)**. A nota final é composta por 5 avaliações distribuídas ao longo das 14 quinzenas:

| Avaliação | Peso | Quinzena | Entrega |
|-----------|------|----------|----------|
| Plano de Ação | 15% | 2 | Documento estruturado com programação de atividades |
| Relatório Parcial | 25% | 7 | Documento acadêmico ABNT (intro, metodologia, solução inicial) |
| Relatório Final | 35% | 14 | Documento completo com protótipo e aplicação |
| Vídeo + Ficha | 10% | 14 | Vídeo 5-10min no YouTube + Ficha de Prototipagem |
| Avaliação Colaborativa | 15% | 13 | Reunião com orientador (auto e heteroavaliação) |

**Total:** 100%

---

### 13.2. Mapeamento de Requisitos x Critérios de Avaliação

Cada avaliação possui rubricas específicas. A equipe deve garantir que os requisitos deste documento atendam aos critérios:

#### ✅ **Avaliação 1: Plano de Ação (Quinzena 2)**

**Requisitos relacionados:** Todos os requisitos devem aparecer no cronograma

**Critérios-chave:**
- ❌ **3,0 pontos:** Planejamento completo de TODAS as quinzenas com atividades, responsáveis, datas e descrições
- ❌ **Obrigatório:** Todos os 7 integrantes devem ter atividades distribuídas em todas as semanas
- ❌ **Relação com tema norteador:** Explicitar como o projeto (Carteira Digital de Vacinação PET) se relaciona com o tema da UNIVESP

**Ações da equipe:**
- Int 1 (Líder): Consolidar Plano de Ação com input de todos
- Int 7 (Documentador): Formatar e garantir clareza do português
- Todos: Revisar e validar suas responsabilidades antes da entrega

---

#### 📝 **Avaliação 2: Relatório Parcial (Quinzena 7)**

**Requisitos relacionados:** 
- Requisitos Funcionais (Seção 3): Base para definir objetivos
- Casos de Uso (Seção 5): Ilustram metodologia
- Modelo de Dados (Seção 6): Fundamentação técnica

**Critérios-chave:**
- ❌ **2,0 pontos:** Fundamentação teórica com fontes confiáveis (artigos, livros, teses)
  - ➡️ Já temos 17 referências na Seção 14 deste documento
- ❌ **1,5 pontos:** Metodologia com Design Thinking (ouvir, criar, prototipar)
  - ➡️ Fase de Empatia: Int 6 conduz entrevistas (7-10 usuários)
  - ➡️ Fase de Criação: Wireframes (Int 5) + Diagrama ER (Int 4)
  - ➡️ Fase de Prototipar: MVP inicial (Int 3 + Int 4 + Int 5)
- ❌ **1,5 pontos:** Solução inicial com **primeira aplicação do protótipo**
  - ➡️ Até Quinzena 7: MVP com RF01-RF05 (Autenticação + Cadastro Pet + Vacinas básico)

**Distribuição de responsabilidades:**
- Int 1: Introdução e objetivos
- Int 6: Justificativa e problema de pesquisa (baseado nas entrevistas)
- Int 7: Fundamentação teórica (usar referências da Seção 14)
- Int 2: Metodologia (Design Thinking + Scrum + tecnologias)
- Int 3 + Int 5: Solução inicial (screenshots do protótipo funcionando)
- Int 7: Linguagem e referências (ABNT, revisão final)

---

#### 📄 **Avaliação 3: Relatório Final (Quinzena 14)**

**ATENÇÃO CRÍTICA:** É **OBRIGATÓRIO** descrever o protótipo realizado e sua aplicação. Sem isso, nota = **ZERO**.

**Requisitos relacionados:** TODOS os requisitos (RF01-RF19, RNF01-RNF12)

**Critérios-chave:**
- ❌ **2,0 pontos:** Relação com **mais de 3 disciplinas** da UNIVESP
  - ➡️ Sugestões: Engenharia de Software, Banco de Dados, Lógica de Programação, Desenvolvimento Web, Projeto Integrador, Matemática Computacional, Interação Humano-Computador
  - ➡️ Int 1 + Int 7: Identificar disciplinas cursadas e mapear conteúdos usados
- ❌ **2,0 pontos:** Adequação ao Design Thinking (ouvir, prototipar, implementar)
  - ➡️ Int 6: Documentar fase "Ouvir" (entrevistas, personas, mapa de empatia)
  - ➡️ Int 2 + Int 3 + Int 4 + Int 5: Documentar "Prototipar" (wireframes → MVP)
  - ➡️ Int 1 + Int 6: Documentar "Implementar" (testes com usuários reais, feedbacks)
- ❌ **3,0 pontos:** Solução final com **descrição detalhada + imagens** + **melhorias a partir de feedbacks**
  - ➡️ Int 5: Capturas de tela de TODAS as funcionalidades (RF01-RF19)
  - ➡️ Int 6: Relatório de testes com usuários (fase Quinzena 11-12)
  - ➡️ Int 7: Compilar melhorias implementadas (antes vs depois)

**Checklist de Conformidade:**
- [ ] Título sintetiza o projeto (0,5 pt)
- [ ] Resumo até 250 palavras (estrutura)
- [ ] Introdução menciona disciplinas da UNIVESP (2,0 pt)
- [ ] Design Thinking completo documentado (2,0 pt)
- [ ] Solução final descrita COM IMAGENS (3,0 pt)
- [ ] Feedbacks da comunidade documentados (parte dos 3,0 pt)
- [ ] Considerações finais com balanço inicial vs final (0,5 pt)
- [ ] Capa, sumário, resumo, palavras-chave, referências ABNT (1,0 pt)
- [ ] Correções do Relatório Parcial implementadas (1,0 pt)

---

#### 🎬 **Avaliação 4: Vídeo + Ficha de Prototipagem (Quinzena 14)**

**Requisitos relacionados:** Demonstração visual dos RF01-RF19

**Critérios-chave:**
- ❌ **3,0 pontos:** Solução apresentada **EM FUNCIONAMENTO** (não apenas slides)
  - ➡️ Int 3 + Int 5: Preparar ambiente de demonstração (localhost ou deploy)
  - ➡️ Int 5: Gravar navegação pelas telas principais
    - Login (RF01)
    - Cadastro de Pet (RF04)
    - Registro de Vacina (RF07-RF08)
    - Visualização de Histórico (RF10)
    - Alertas (RF12)
- ❌ **2,0 pontos:** Implementação na comunidade externa + **impactos**
  - ➡️ Int 6: Conduzir testes com 3-5 donos de pets (Quinzena 11-12)
  - ➡️ Int 1: Relatar mudanças/melhorias no sistema baseadas nos testes
- ❌ **2,0 pontos:** Recursos variados (slides + imagens + vídeos externos)
  - ➡️ Int 5: Editar vídeo com: 
    - Slides iniciais (identificação, problema)
    - Screencast do sistema funcionando
    - Depoimentos de usuários (opcional, mas recomendado)
- ❌ **1,0 ponto:** Tempo **5-10 minutos** (nem mais, nem menos)
  - ➡️ Ensaiar antes, cronometrar

**Estrutura sugerida do vídeo (9 minutos):**
1. Identificação (30s): Nomes, tema, polo
2. Problema (1min): Contexto, dor dos usuários
3. Solução proposta (30s): Visão geral do sistema
4. Demonstração (5min): Sistema funcionando (navegação pelas funcionalidades)
5. Testes com usuários (1min): Feedbacks coletados, melhorias feitas
6. Tecnologias (30s): Flask, SQLAlchemy, Bootstrap
7. Conclusão (30s): Impacto, próximos passos

**Responsáveis:**
- Int 5: Criação e edição do vídeo
- Int 1 + Int 6: Roteiro e narração
- Int 3: Demonstração técnica do sistema
- Todos: Revisar antes de publicar

---

#### 🤝 **Avaliação 5: Avaliação Colaborativa (Quinzena 13)**

**Objetivo:** Avaliar desempenho individual de cada integrante.

**Critérios-chave:**
- ❌ **5,0 pontos:** Nota do grupo (definir 3 critérios de avaliação)
  - ➡️ Sugestões de critérios:
    1. **Cumprimento de prazos:** Entregou atividades no prazo acordado? (0-2 pts)
    2. **Qualidade das entregas:** Trabalho bem feito, revisado, funcional? (0-2 pts)
    3. **Colaboração:** Ajudou outros, participou de reuniões, comunicou-se bem? (0-1 pt)
- ❌ **5,0 pontos:** Nota do orientador
  - ➡️ **Para pontuar bem:**
    - Comunicar-se FREQUENTEMENTE com orientador (não esperar ele perguntar)
    - Seguir o Plano de Ação à risca
    - Demonstrar interesse e proatividade
    - Pedir ajuda quando necessário

**Evidências de participação (preparar para Quinzena 13):**
- Histórico de commits no GitHub (com mensagens claras)
- Atas de reuniões (Int 7 documenta)
- E-mails/mensagens trocados com orientador
- Artefatos produzidos (wireframes, código, documentação)

**Responsável:** Int 1 organiza reunião, Int 7 documenta processo

---

### 13.3. Estratégia da Equipe para Maximizar Nota

**Pontos fortes deste documento que já atendem aos critérios:**
- ✅ Requisitos funcionais detalhados (RF01-RF19) → facilita descrição da solução
- ✅ Casos de uso com fluxos → ilustra metodologia
- ✅ Modelo de dados completo → fundamentação técnica
- ✅ Arquitetura definida → demonstra conhecimento de engenharia de software
- ✅ 17 referências ABNT → base para fundamentação teórica
- ✅ Distribuição de responsabilidades clara (Seção 12) → facilita Plano de Ação

**O que ainda precisa ser feito (ao longo das 14 quinzenas):**
- ❌ **Quinzena 1-2:** Entrevistas com usuários (Design Thinking - Ouvir)
- ❌ **Quinzena 2:** Elaborar Plano de Ação completo com cronograma
- ❌ **Quinzena 3-6:** Desenvolver MVP (prototipar)
- ❌ **Quinzena 7:** Primeira entrega (Relatório Parcial)
- ❌ **Quinzena 7-10:** Completar todos os requisitos (RF01-RF19)
- ❌ **Quinzena 11-12:** Testes com usuários reais (coletar feedbacks)
- ❌ **Quinzena 13:** Avaliação Colaborativa (reunião com orientador)
- ❌ **Quinzena 14:** Relatório Final + Vídeo

**Alertas importantes:**
- ⚠️ **PLÁGIO = ZERO:** Nunca copiar texto de outros trabalhos sem citação
- ⚠️ **TEMA NORTEADOR:** Sempre explicitar relação com o tema definido pela UNIVESP
- ⚠️ **COMUNIDADE EXTERNA:** Obrigatório testar com usuários reais e documentar
- ⚠️ **DESIGN THINKING:** Documentar TODAS as fases (não é opcional)
- ⚠️ **PROTÓTIPO FUNCIONAL:** Vídeo deve mostrar sistema EM FUNCIONAMENTO

---

## 14. CONCLUSÃO

Este documento apresentou a análise completa de requisitos do sistema **Carteira Digital de Vacinação para PET**, desenvolvido colaborativamente por uma equipe de 7 integrantes.

O projeto visa desenvolver uma solução web moderna, intuitiva e segura para gerenciamento de informações de saúde de animais de estimação, seguindo a metodologia Design Thinking e práticas ágeis de desenvolvimento.

**Diferencia is do projeto em equipe:**
- ✅ Especialização de papéis (cada integrante foca em sua área de expertise)
- ✅ Distribuição equilibrada de carga (~18-20h por pessoa)
- ✅ Qualidade superior através de code review e validações cruzadas
- ✅ Desenvolvimento mais rápido (paralelização de tarefas)
- ✅ Aprendizado colaborativo (workshops internos)

**Conformidade com PJI110:**
- ✅ Resolução de um problema real (validado com 7-10 entrevistas)
- ✅ Desenvolvimento web com framework (Flask)
- ✅ Uso de HTML e CSS (Bootstrap)
- ✅ Banco de dados relacional (SQLite/PostgreSQL)
- ✅ Controle de versão (Git com Git Flow)
- ✅ Trabalho em equipe estruturado

**Alinhamento com Critérios de Avaliação Oficiais (Seção 13):**
- ✅ Estrutura completa para suportar Plano de Ação (15% da nota)
- ✅ Fundamentação teórica robusta com 18 referências para Relatório Parcial (25%)
- ✅ Requisitos detalhados (RF01-RF19) para descrição completa no Relatório Final (35%)
- ✅ Roadmap de demonstração para Vídeo + Ficha (10%)
- ✅ Distribuição clara de responsabilidades para Avaliação Colaborativa (15%)

A implementação seguirá as boas práticas de engenharia de software, com foco em usabilidade, segurança, manutenibilidade e colaboração efetiva entre os integrantes, garantindo conformidade total com as **Orientações Oficiais da UNIVESP para Avaliação do Projeto Integrador**.

---

## 15. REFERÊNCIAS

**Responsável pela pesquisa e formatação:** Integrante 7 (Documentador)

### Normativas e Regulamentos:

UNIVERSIDADE VIRTUAL DO ESTADO DE SÃO PAULO. **Orientações para a avaliação do Projeto Integrador.** UNIVESP, set. 2022. 13 p.

### Metodologia e Gestão:

CASALE, A. **Aprendizagem baseada em problemas:** desenvolvimento de competências para o ensino em engenharia. 2013. Tese (Doutorado em Engenharia de Produção) – Escola de Engenharia de São Carlos, Universidade de São Paulo, São Paulo, 2013.

GERHARDT, T. E; SILVEIRA, D. T. **Métodos de pesquisa.** Porto Alegre: Editora UFRGS, 2009.

CAVALCANTI, C. M. C. **Design Thinking como metodologia de pesquisa para concepção de um ambiente virtual de aprendizagem centrado no usuário.** 2015. Dissertação (Mestrado) – Universidade Federal de Pernambuco, Recife, 2015.

SCHWABER, K.; SUTHERLAND, J. **The Scrum Guide.** Scrum.org, 2020. Disponível em: https://scrumguides.org/. Acesso em: 01 mar. 2026.

### Engenharia de Software:

YIN, R. K. **Estudo de caso:** planejamento e métodos. Porto Alegre: Bookman, 2015.

SOMMERVILLE, I. **Engenharia de Software.** 10ª ed. São Paulo: Pearson, 2018.

PRESSMAN, R. S.; MAXIM, B. R. **Engenharia de Software:** Uma Abordagem Profissional. 8ª ed. Porto Alegre: McGraw Hill, 2016.

MARTIN, R. C. **Clean Code:** A Handbook of Agile Software Craftsmanship. Upper Saddle River: Prentice Hall, 2008.

### Tecnologias Web:

FLASK DOCUMENTATION. **Flask Web Development.** Disponível em: https://flask.palletsprojects.com/. Acesso em: 01 mar. 2026.

GRINBERG, M. **Flask Web Development:** Developing Web Applications with Python. 2nd ed. Sebastopol: O'Reilly Media, 2018.

SQLALCHEMY DOCUMENTATION. **SQLAlchemy - The Database Toolkit for Python.** Disponível em: https://www.sqlalchemy.org/. Acesso em: 01 mar. 2026.

BOOTSTRAP DOCUMENTATION. **Bootstrap - The most popular HTML, CSS, and JS library.** Disponível em: https://getbootstrap.com/. Acesso em: 01 mar. 2026.

### Banco de Dados:

DATE, C. J. **Introdução a Sistemas de Bancos de Dados.** 8ª ed. Rio de Janeiro: Campus, 2004.

ELMASRI, R.; NAVATHE, S. B. **Sistemas de Banco de Dados.** 6ª ed. São Paulo: Pearson, 2011.

### Design e UX:

BROWN, T. **Design Thinking:** uma metodologia poderosa para decretar o fim das velhas ideias. Rio de Janeiro: Elsevier, 2010.

GARRETT, J. J. **The Elements of User Experience:** User-Centered Design for the Web and Beyond. 2nd ed. Berkeley: New Riders, 2010.

### Controle de Versão:

CHACON, S.; STRAUB, B. **Pro Git.** 2nd ed. Apress, 2014. Disponível em: https://git-scm.com/book/pt-br/v2. Acesso em: 01 mar. 2026.

---

**Documento elaborado por:**  
Equipe de 7 Integrantes - Projeto Integrador PJI110 UNIVESP

**Principais colaboradores na elaboração:**
- Análise de Requisitos: Integrante 6 (Analista)
- Modelagem de Dados: Integrante 4 (BD)
- Arquitetura: Integrante 2 (Arquiteto)
- Wireframes: Integrante 5 (Frontend)
- Consolidação e Formatação: Integrante 7 (Documentador)
- Revisão Geral: Integrante 1 (Líder)

**Data:** 02/03/2026  
**Versão:** 2.0 (Equipe)  
**Status:** Aprovado por todos os 7 integrantes

---

## CONTROLE DE VERSÕES

| Versão | Data | Responsável | Alterações |
|--------|------|-------------|------------|
| 1.0 | 01/03/2026 | Versão Individual | Documento base criado |
| 2.0 | 02/03/2026 | Equipe (7 integrantes) | Adaptação para trabalho em equipe: distribuição de papéis, responsabilidades, cronograma colaborativo |
| 2.1 | 02/03/2026 | Integrante 7 (Documentador) | Adição da Seção 13 (Critérios de Avaliação) conforme Orientações Oficiais UNIVESP; mapeamento de requisitos x critérios; estratégias para maximizar nota; adição de referência ao documento oficial |

**Próxima revisão planejada:** Semana 4 (após feedback do professor)
