# ANÁLISE DE REQUISITOS DO SISTEMA
## Carteira Digital de Vacinação para PET

**Disciplina:** PJI110 - Projeto Integrador em Computação I  
**Instituição:** UNIVESP - Universidade Virtual do Estado de São Paulo  
**Data:** Março de 2026

---

## 1. INTRODUÇÃO

### 1.1 Propósito do Documento
Este documento apresenta a análise de requisitos do sistema **Carteira Digital de Vacinação para PET**, detalhando as funcionalidades, características técnicas e restrições do projeto. O objetivo é fornecer uma visão clara e completa do sistema a ser desenvolvido.

### 1.2 Escopo do Projeto
O sistema proposto é uma aplicação web que permite aos donos de animais de estimação (pets) gerenciar de forma digital o histórico completo de vacinação e saúde de seus animais, substituindo as tradicionais carteirinhas de papel.

### 1.3 Definições e Abreviações
- **Pet:** Animal de estimação
- **Tutor:** Dono/responsável pelo pet
- **MVP:** Minimum Viable Product (Produto Mínimo Viável)
- **CRUD:** Create, Read, Update, Delete (Criar, Ler, Atualizar, Deletar)

---

## 2. DESCRIÇÃO GERAL DO SISTEMA

### 2.1 Perspectiva do Produto
A Carteira Digital de Vacinação para PET é um sistema web independente que visa modernizar o controle de saúde animal, oferecendo uma alternativa digital, segura e acessível às carteiras de vacinação físicas.

### 2.2 Funções do Produto
O sistema permitirá:
- Cadastro e autenticação de tutores
- Gerenciamento de múltiplos pets por tutor
- Registro completo do histórico de vacinação
- Visualização organizada dos dados de saúde
- Alertas automáticos sobre vacinas próximas do vencimento
- Acesso multiplataforma (computador, tablet, celular)

### 2.3 Características dos Usuários

| Tipo de Usuário | Descrição | Conhecimento Técnico |
|-----------------|-----------|---------------------|
| Tutor de Pet | Pessoa física, dono de animal de estimação | Básico (uso de internet) |
| Administrador | Responsável pela manutenção do sistema | Avançado (técnico) |

### 2.4 Restrições
- Sistema web (requer conexão com internet)
- Desenvolvido com tecnologias gratuitas e open-source
- Prazo de desenvolvimento: 14 semanas
- Interface em português brasileiro
- Compatível com navegadores modernos (Chrome, Firefox, Edge)

---

## 3. REQUISITOS FUNCIONAIS

### 3.1 Módulo de Autenticação

**RF01 - Cadastro de Usuário**
- **Descrição:** O sistema deve permitir que novos tutores criem uma conta
- **Entrada:** Nome completo, e-mail, senha, confirmação de senha
- **Processo:** Validação de dados, verificação de e-mail único, criptografia de senha
- **Saída:** Conta criada com sucesso ou mensagem de erro
- **Prioridade:** Alta

**RF02 - Login de Usuário**
- **Descrição:** O sistema deve autenticar tutores cadastrados
- **Entrada:** E-mail e senha
- **Processo:** Verificação de credenciais no banco de dados
- **Saída:** Acesso ao sistema ou mensagem de erro
- **Prioridade:** Alta

**RF03 - Logout**
- **Descrição:** O sistema deve permitir que o usuário encerre sua sessão
- **Entrada:** Comando de logout
- **Processo:** Encerrar sessão ativa
- **Saída:** Retorno à tela de login
- **Prioridade:** Alta

**RF04 - Recuperação de Senha**
- **Descrição:** O sistema deve permitir recuperação de senha via e-mail
- **Entrada:** E-mail cadastrado
- **Processo:** Envio de link de redefinição
- **Saída:** E-mail enviado ou mensagem de erro
- **Prioridade:** Média

### 3.2 Módulo de Gerenciamento de Pets

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
  - Foto (opcional)
- **Processo:** Validação e armazenamento dos dados
- **Saída:** Pet cadastrado com sucesso
- **Prioridade:** Alta

**RF06 - Listar Pets**
- **Descrição:** O tutor visualiza todos os seus pets cadastrados
- **Entrada:** Usuário autenticado
- **Processo:** Buscar pets do usuário no banco de dados
- **Saída:** Lista com cards/resumo de cada pet
- **Prioridade:** Alta

**RF07 - Visualizar Detalhes do Pet**
- **Descrição:** Exibir informações completas de um pet específico
- **Entrada:** Seleção de um pet
- **Processo:** Buscar dados completos do pet
- **Saída:** Página com todos os dados e histórico
- **Prioridade:** Alta

**RF08 - Editar Pet**
- **Descrição:** O tutor pode atualizar informações do pet
- **Entrada:** Novos dados do pet
- **Processo:** Validação e atualização no banco
- **Saída:** Dados atualizados com sucesso
- **Prioridade:** Média

**RF09 - Excluir Pet**
- **Descrição:** O tutor pode remover um pet do sistema
- **Entrada:** Confirmação de exclusão
- **Processo:** Remoção do pet e dados relacionados
- **Saída:** Pet excluído com sucesso
- **Prioridade:** Média

### 3.3 Módulo de Vacinação

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
- **Prioridade:** Alta

**RF11 - Visualizar Histórico de Vacinas**
- **Descrição:** Exibir todas as vacinas do pet em ordem cronológica
- **Entrada:** Pet selecionado
- **Processo:** Buscar vacinas do pet no banco
- **Saída:** Lista ordenada por data
- **Prioridade:** Alta

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

**RF15 - Alertas de Vacinas Próximas**
- **Descrição:** Notificar sobre vacinas com vencimento próximo
- **Entrada:** Sistema verifica datas automaticamente
- **Processo:** Comparar data atual com próximas doses
- **Saída:** Avisos na dashboard e/ou por e-mail
- **Prioridade:** Média

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

### 3.5 Funcionalidades Adicionais (Opcionais)

**RF17 - Upload de Documentos**
- **Descrição:** Anexar exames e documentos veterinários
- **Prioridade:** Baixa

**RF18 - Gerar Carteirinha em PDF**
- **Descrição:** Exportar carteirinha de vacinação em PDF
- **Prioridade:** Baixa

**RF19 - Compartilhar Carteirinha**
- **Descrição:** Gerar link público para visualização
- **Prioridade:** Baixa

---

## 4. REQUISITOS NÃO-FUNCIONAIS

### 4.1 Requisitos de Usabilidade

**RNF01 - Interface Intuitiva**
- O sistema deve ter navegação clara e autoexplicativa
- Máximo de 3 cliques para acessar qualquer funcionalidade principal

**RNF02 - Responsividade**
- Interface deve se adaptar a diferentes tamanhos de tela
- Compatível com dispositivos móveis (smartphones e tablets)

**RNF03 - Feedback Visual**
- Todas as ações devem ter confirmação visual clara
- Mensagens de erro devem ser descritivas e úteis

### 4.2 Requisitos de Desempenho

**RNF04 - Tempo de Resposta**
- Páginas principais devem carregar em até 3 segundos
- Operações no banco devem responder em até 1 segundo

**RNF05 - Capacidade**
- Sistema deve suportar pelo menos 100 usuários simultâneos
- Cada usuário pode ter até 20 pets cadastrados

### 4.3 Requisitos de Segurança

**RNF06 - Autenticação**
- Senhas devem ser armazenadas com hash (bcrypt ou similar)
- Sessões devem expirar após 24h de inatividade

**RNF07 - Autorização**
- Usuários só podem acessar dados dos próprios pets
- Proteção contra SQL Injection e XSS

**RNF08 - Privacidade**
- Dados pessoais devem seguir boas práticas de privacidade
- Opção de exclusão completa da conta

### 4.4 Requisitos de Confiabilidade

**RNF09 - Disponibilidade**
- Sistema deve estar disponível 95% do tempo
- Backup automático do banco de dados

**RNF10 - Recuperação de Erros**
- Mensagens de erro claras sem expor informações técnicas
- Log de erros para depuração

### 4.5 Requisitos de Manutenibilidade

**RNF11 - Código Limpo**
- Código comentado e documentado
- Seguir boas práticas de programação (PEP 8 para Python)

**RNF12 - Versionamento**
- Código versionado com Git
- Commits descritivos e organizados

---

## 5. CASOS DE USO

### UC01: Cadastrar Novo Pet

**Ator Principal:** Tutor do Pet  
**Pré-condições:** Usuário deve estar autenticado  

**Fluxo Principal:**
1. Tutor acessa página "Meus Pets"
2. Tutor clica em "Adicionar Novo Pet"
3. Sistema exibe formulário de cadastro
4. Tutor preenche dados obrigatórios (nome, espécie)
5. Tutor opcionalmente adiciona foto
6. Tutor clica em "Salvar"
7. Sistema valida dados
8. Sistema armazena pet no banco de dados
9. Sistema exibe mensagem de sucesso
10. Sistema redireciona para lista de pets

**Fluxos Alternativos:**
- **3a.** Dados inválidos ou incompletos:
  - Sistema exibe mensagens de erro
  - Usuário corrige dados e tenta novamente

**Pós-condições:** Novo pet cadastrado e visível na lista

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
4. Sistema exibe formulário
5. Tutor preenche dados da vacina
6. Tutor define data da próxima dose (se aplicável)
7. Tutor clica em "Salvar"
8. Sistema valida dados
9. Sistema armazena vacina
10. Sistema atualiza histórico
11. Sistema cria alerta para próxima dose (se informada)

**Fluxos Alternativos:**
- **5a.** Data futura inválida:
  - Sistema impede data de aplicação futura
  - Exibe mensagem de erro

**Pós-condições:** Vacina registrada e visível no histórico

---

### UC03: Consultar Vacinas Pendentes

**Ator Principal:** Tutor do Pet  
**Pré-condições:** Usuário autenticado

**Fluxo Principal:**
1. Tutor acessa dashboard
2. Sistema busca vacinas com próxima dose agendada
3. Sistema compara com data atual
4. Sistema exibe lista de vacinas pendentes/próximas
5. Sistema destaca vacinas atrasadas em vermelho
6. Tutor pode clicar em uma vacina para ver detalhes

**Pós-condições:** Tutor informado sobre status das vacinas

---

## 6. MODELO DE DADOS

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
         │ 1:N
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
         │ 1:N
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

### 6.2 Dicionário de Dados

**Tabela: usuarios**

| Campo | Tipo | Tamanho | Restrições | Descrição |
|-------|------|---------|------------|-----------|
| id | INTEGER | - | PK, AUTO_INCREMENT | Identificador único |
| nome | VARCHAR | 100 | NOT NULL | Nome completo do tutor |
| email | VARCHAR | 120 | NOT NULL, UNIQUE | E-mail para login |
| senha_hash | VARCHAR | 255 | NOT NULL | Senha criptografada |
| data_cadastro | DATETIME | - | NOT NULL, DEFAULT NOW | Data de registro |

**Tabela: pets**

| Campo | Tipo | Tamanho | Restrições | Descrição |
|-------|------|---------|------------|-----------|
| id | INTEGER | - | PK, AUTO_INCREMENT | Identificador único |
| usuario_id | INTEGER | - | FK, NOT NULL | Dono do pet |
| nome | VARCHAR | 50 | NOT NULL | Nome do pet |
| especie | VARCHAR | 30 | NOT NULL | Cão, gato, etc. |
| raca | VARCHAR | 50 | NULL | Raça do animal |
| data_nascimento | DATE | - | NULL | Data de nascimento |
| sexo | VARCHAR | 10 | NULL | Macho/Fêmea |
| peso | DECIMAL | 5,2 | NULL | Peso em kg |
| cor | VARCHAR | 30 | NULL | Cor predominante |
| foto_path | VARCHAR | 255 | NULL | Caminho da foto |
| data_cadastro | DATETIME | - | NOT NULL, DEFAULT NOW | Data de cadastro |

**Tabela: vacinas**

| Campo | Tipo | Tamanho | Restrições | Descrição |
|-------|------|---------|------------|-----------|
| id | INTEGER | - | PK, AUTO_INCREMENT | Identificador único |
| pet_id | INTEGER | - | FK, NOT NULL | Pet vacinado |
| nome_vacina | VARCHAR | 100 | NOT NULL | Nome da vacina |
| data_aplicacao | DATE | - | NOT NULL | Quando foi aplicada |
| veterinario | VARCHAR | 100 | NULL | Nome do veterinário |
| clinica | VARCHAR | 100 | NULL | Nome da clínica |
| lote | VARCHAR | 50 | NULL | Lote da vacina |
| proxima_dose | DATE | - | NULL | Data da próxima dose |
| observacoes | TEXT | - | NULL | Informações adicionais |
| data_registro | DATETIME | - | NOT NULL, DEFAULT NOW | Quando foi registrado |

---

## 7. ARQUITETURA DO SISTEMA

### 7.1 Arquitetura de Alto Nível

```
┌─────────────────────────────────────────┐
│         CAMADA DE APRESENTAÇÃO          │
│  (HTML, CSS, Bootstrap, JavaScript)     │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│        CAMADA DE APLICAÇÃO              │
│     (Flask - Framework Web Python)      │
│  - Routes (URLs)                        │
│  - Controllers (Lógica)                 │
│  - Forms (Validações)                   │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│        CAMADA DE NEGÓCIO                │
│     (Models - SQLAlchemy ORM)           │
│  - Usuario                              │
│  - Pet                                  │
│  - Vacina                               │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│        CAMADA DE DADOS                  │
│    (SQLite / PostgreSQL)                │
└─────────────────────────────────────────┘
```

### 7.2 Tecnologias Utilizadas

**Backend:**
- Python 3.8+
- Flask (Framework web)
- Flask-SQLAlchemy (ORM - banco de dados)
- Flask-Login (Autenticação)
- Flask-WTF (Formulários e validação)
- Werkzeug (Segurança - hash de senhas)

**Frontend:**
- HTML5
- CSS3
- Bootstrap 5 (Framework CSS responsivo)
- JavaScript (interações básicas)

**Banco de Dados:**
- SQLite (Desenvolvimento)
- PostgreSQL (Produção - opcional)

**Controle de Versão:**
- Git
- GitHub

**Ferramentas de Desenvolvimento:**
- Visual Studio Code
- Git Bash / PowerShell
- DB Browser for SQLite (visualizar banco)

---

## 8. INTERFACE DO USUÁRIO (WIREFRAMES)

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

---

## 9. REGRAS DE NEGÓCIO

**RN01:** Um usuário só pode visualizar e gerenciar seus próprios pets  
**RN02:** Um pet pode ter apenas um dono (usuário)  
**RN03:** Um pet pode ter múltiplas vacinas registradas  
**RN04:** Data de aplicação de vacina não pode ser futura  
**RN05:** Email de usuário deve ser único no sistema  
**RN06:** Senha deve ter no mínimo 6 caracteres  
**RN07:** Nome do pet é obrigatório  
**RN08:** Espécie do pet é obrigatória  
**RN09:** Ao excluir um pet, todas as vacinas relacionadas são excluídas (cascade)  
**RN10:** Ao excluir um usuário, todos os pets e vacinas relacionados são excluídos  
**RN11:** Alertas são gerados para vacinas com próxima dose em até 15 dias  
**RN12:** Fotos de pets devem ter tamanho máximo de 5MB  
**RN13:** Formatos de imagem aceitos: JPG, PNG, GIF

---

## 10. CRONOGRAMA DE DESENVOLVIMENTO

| Fase | Semanas | Atividades | Entregas |
|------|---------|------------|----------|
| **Planejamento** | 1-2 | Análise de requisitos, setup do ambiente, criação do repositório | Plano de Ação, Documento de Requisitos |
| **Levantamento** | 3-4 | Pesquisa bibliográfica, definição de tecnologias, modelagem do banco | Levantamento Bibliográfico |
| **Desenvolvimento I** | 5-6 | Implementação de autenticação, CRUD de pets | Protótipo funcional básico |
| **Desenvolvimento II** | 7-8 | Sistema de vacinas, alertas, melhorias de interface | Relatório Parcial + Demo |
| **Testes e Ajustes** | 9-12 | Testes, correção de bugs, funcionalidades extras, documentação | Sistema completo |
| **Finalização** | 13-14 | Documentação final, vídeo de apresentação, deploy | Relatório Final + Vídeo + Sistema |

---

## 11. RISCOS E MITIGAÇÕES

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Falta de experiência com Flask | Alta | Médio | Estudar tutoriais, documentação oficial, buscar suporte em fóruns |
| Problemas com banco de dados | Média | Alto | Usar SQLite (mais simples), fazer backups frequentes |
| Dificuldade com CSS/Design | Média | Baixo | Usar Bootstrap (framework pronto), templates gratuitos |
| Atraso no cronograma | Média | Alto | Priorizar funcionalidades essenciais (MVP), deixar extras opcionais |
| Bugs de segurança | Baixa | Alto | Seguir boas práticas, usar bibliotecas confiáveis, validação rigorosa |
| Perda de código | Baixa | Alto | Git + GitHub (versionamento), commits frequentes |

---

## 12. CONCLUSÃO

Este documento apresentou a análise completa de requisitos do sistema **Carteira Digital de Vacinação para PET**. O projeto visa desenvolver uma solução web moderna, intuitiva e segura para gerenciamento de informações de saúde de animais de estimação.

O sistema atende aos objetivos da disciplina PJI110, contemplando:
- ✅ Resolução de um problema real
- ✅ Desenvolvimento web com framework (Flask)
- ✅ Uso de HTML e CSS
- ✅ Banco de dados relacional
- ✅ Controle de versão (Git)

A implementação seguirá as boas práticas de engenharia de software, com foco em usabilidade, segurança e manutenibilidade do código.

---

## 13. REFERÊNCIAS

CASALE, A. **Aprendizagem baseada em problemas:** desenvolvimento de competências para o ensino em engenharia. 2013. Tese (Doutorado em Engenharia de Produção) – Escola de Engenharia de São Carlos, Universidade de São Paulo, São Paulo, 2013.

GERHARDT, T. E; SILVEIRA, D. T. **Métodos de pesquisa.** Porto Alegre: Editora UFRGS, 2009.

YIN, R. K. **Estudo de caso:** planejamento e métodos. Porto Alegre: Bookman, 2015.

FLASK DOCUMENTATION. **Flask Web Development.** Disponível em: https://flask.palletsprojects.com/. Acesso em: 01 mar. 2026.

SQLALCHEMY DOCUMENTATION. **SQLAlchemy - The Database Toolkit for Python.** Disponível em: https://www.sqlalchemy.org/. Acesso em: 01 mar. 2026.

BOOTSTRAP DOCUMENTATION. **Bootstrap - The most popular HTML, CSS, and JS library.** Disponível em: https://getbootstrap.com/. Acesso em: 01 mar. 2026.

---

**Documento elaborado por:** [Seu Nome]  
**Data:** 01/03/2026  
**Versão:** 1.0
