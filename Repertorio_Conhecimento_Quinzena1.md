# REPERTÓRIO DE CONHECIMENTO - QUINZENA 1
## PJI110 - Projeto Integrador em Computação I
### Demonstração de Domínio dos Conteúdos

**Data:** Março 2026  
**Aluna:** [SEU NOME]  
**Tema do Projeto:** Carteira Digital de Vacinação para PET

---

## 📚 ÍNDICE DE CONHECIMENTOS

1. [Metodologias de Desenvolvimento](#1-metodologias-de-desenvolvimento)
2. [Design Thinking](#2-design-thinking)
3. [Engenharia de Software](#3-engenharia-de-software)
4. [Tecnologias Web](#4-tecnologias-web)
5. [Banco de Dados](#5-banco-de-dados)
6. [Controle de Versão](#6-controle-de-versão)
7. [Gestão de Projetos](#7-gestão-de-projetos)
8. [Domínio do Problema](#8-domínio-do-problema)

---

## 1. METODOLOGIAS DE DESENVOLVIMENTO

### 1.1 Aprendizagem Baseada em Problemas (ABP)

**O que é:**
A ABP é uma metodologia de ensino-aprendizagem que utiliza problemas reais como ponto de partida para a aquisição de novos conhecimentos. Em vez de primeiro estudar teoria e depois aplicar, invertemos: identificamos um problema real e buscamos os conhecimentos necessários para resolvê-lo.

**Como aplico no meu projeto:**
- **Problema identificado:** Carteiras de vacinação em papel se perdem, não há sistema de alertas
- **Conhecimentos que preciso adquirir:**
  - Desenvolvimento web com Flask
  - Modelagem de banco de dados
  - Interface responsiva com Bootstrap
  - Sistema de notificações
  - Segurança de dados e autenticação
- **Aprendizado ativo:** Estou estudando conforme preciso implementar funcionalidades

**Por que escolhi esse problema:**
1. É um problema **real** que afeta milhões de brasileiros (140+ milhões de pets)
2. Tem **público-alvo definido** (donos de pets)
3. Solução é **tecnicamente viável** com as ferramentas da disciplina
4. Permite aplicar **múltiplas competências** (web, BD, segurança)
5. Tem **impacto social** na saúde preventiva animal

**Vantagens da ABP que já experimentei:**
- ✅ Maior motivação (estou resolvendo algo útil)
- ✅ Aprendizado contextualizado (sei POR QUÊ estou aprendendo Flask)
- ✅ Desenvolvimento de autonomia (busco as soluções)
- ✅ Conexão teoria-prática imediata

---

### 1.2 Trabalho em Equipe e Competências Profissionais

**Meu papel como Engenheira de Computação:**
Entendo que, como futura engenheira, não trabalharei sozinha. Mesmo neste projeto individual, estou desenvolvendo competências essenciais:

**Competências Técnicas:**
- Programação (Python/Flask)
- Modelagem de dados (ER, normalização)
- Arquitetura de software (MVC, camadas)
- Controle de versão (Git/GitHub)
- Testes e qualidade de código

**Competências Profissionais (Soft Skills):**
- **Gestão de tempo:** Cronograma de 2h/dia, 14 semanas
- **Resolução de problemas:** Identificar, analisar, propor soluções
- **Comunicação:** Documentar claramente (README, requisitos)
- **Autonomia:** Buscar soluções em documentações, fóruns
- **Pensamento crítico:** Avaliar tecnologias (Flask vs Django)
- **Adaptabilidade:** Ajustar escopo conforme viabilidade

**Se estivesse em equipe, minha contribuição seria:**
- Backend e banco de dados (minha área de maior interesse)
- Arquitetura do sistema
- Integração entre componentes
- Documentação técnica

---

## 2. DESIGN THINKING

### 2.1 Conceito e Filosofia

**O que é Design Thinking:**
É uma abordagem **centrada no ser humano** para inovação e resolução de problemas. Não começamos com a tecnologia, mas sim entendendo profundamente as pessoas que vão usar nossa solução.

**Princípios que guiam meu projeto:**
1. **Empatia primeiro:** Antes de codificar, entender o dono de pet
2. **Foco no usuário:** Cada decisão pensando na experiência dele
3. **Iteração:** Testar, aprender, melhorar, repetir
4. **Colaboração:** Feedback constante (entrevistas, testes)
5. **Visualização:** Wireframes para tangibilizar ideias

**Por que é importante:**
- Evita criar soluções que ninguém quer usar
- Garante que o sistema resolve o problema REAL
- Reduz retrabalho (validamos antes de construir tudo)
- Aumenta satisfação do usuário final

---

### 2.2 As 5 Fases do Design Thinking (Detalhadas)

#### FASE 1: EMPATIA (👈 ESTAMOS AQUI - Quinzenas 1-2)

**Objetivo:** Compreender profundamente o usuário, suas dores, necessidades e contexto.

**O que estou fazendo:**

**A) Definição do Usuário**
- **Quem é:** Donos de animais de estimação (cães, gatos, etc.)
- **Características:** Pessoas de qualquer idade, que se preocupam com saúde do pet
- **Contexto:** Recebem carteira de papel da clínica veterinária
- **Frustrações:** Perdem carteira, esquecem vacinas, não têm alertas

**B) Perguntas para Entrevistas (que farei)**
1. Como você controla as vacinas do seu pet hoje?
2. Já perdeu ou danificou a carteira de vacinação?
3. Como você lembra das datas das próximas vacinas?
4. Você tem mais de um pet? Como organiza?
5. Usaria um sistema digital? Por quê?
6. Que funcionalidades seriam mais úteis para você?
7. Você acessa mais pelo celular ou computador?
8. Tem alguma dificuldade com tecnologia?

**C) Ferramentas que usarei:**
- **Entrevistas:** Conversar com 3-5 donos de pets
- **Observação:** Ver como controlam hoje (foto da carteira, agenda, etc.)
- **Mapa de Empatia:** Organizar o que pensam, sentem, falam, fazem

**D) Mapa de Empatia (Modelo)**
```
┌─────────────────────────────────────────┐
│  O QUE O USUÁRIO PENSA E SENTE?         │
│  - "Preciso lembrar da vacina"          │
│  - "E se eu perder a carteirinha?"      │
│  - "Tenho 3 gatos, é difícil organizar" │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  O QUE ELE VÊ?                          │
│  - Carteira de papel amarelando         │
│  - Amigos usando apps para tudo         │
│  - Clínicas sem sistema integrado       │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  O QUE ELE FALA E FAZ?                  │
│  - "Sempre esqueço as datas"            │
│  - Coloca lembretes na agenda           │
│  - Tira foto da carteira (backup)       │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  DORES                                   │
│  - Perda de informações                 │
│  - Falta de alertas                     │
│  - Desorganização (múltiplos pets)      │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  GANHOS ESPERADOS                        │
│  - Nunca perder histórico               │
│  - Ser avisado automaticamente          │
│  - Acessar de qualquer lugar            │
└─────────────────────────────────────────┘
```

**Resultado esperado desta fase:**
- Compreensão profunda do usuário ✓
- Lista de dores e necessidades reais ✓
- Insights para próximas fases ✓

---

#### FASE 2: DEFINIÇÃO (Quinzenas 2-3)

**Objetivo:** Sintetizar os aprendizados da empatia em uma definição clara do problema.

**O que farei:**
1. **Analisar dados das entrevistas**
   - Identificar padrões comuns
   - Priorizar necessidades mais citadas

2. **Criar Persona (usuário típico)**
   ```
   Nome: Maria Silva
   Idade: 35 anos
   Profissão: Professora
   Pets: 2 cachorros (Thor e Mel)
   Tecnologia: Usa smartphone diariamente
   Frase: "Adoro meus cachorros, mas é difícil 
           lembrar de todas as vacinas e consultas"
   Dores: Já perdeu carteira 1 vez, esquece datas
   Objetivo: Sistema simples que avise automaticamente
   ```

3. **Declaração do Problema (formato específico)**
   "[MARIA] precisa de [FORMA DE LEMBRAR VACINAS] porque [ESQUECE DATAS E JÁ PERDEU CARTEIRA]"

4. **Priorização de Requisitos**
   - Essenciais (MVP): cadastro, vacinas, alertas
   - Importantes: múltiplos pets, histórico completo
   - Desejáveis: PDF, compartilhamento, anexar documentos

---

#### FASE 3: IDEAÇÃO (Quinzenas 4-5)

**Objetivo:** Gerar o máximo de ideias de solução possível.

**Técnicas que usarei:**

**A) Brainstorming de Funcionalidades**
- Sistema de alertas por email/SMS
- Dashboard visual com calendário
- Lembretes X dias antes da vacina
- Upload de documentos (atestados)
- Geração de PDF da carteira
- QR Code para compartilhar
- Integração com clínicas veterinárias

**B) Wireframes (Esboços de Telas)**
Já criei 4 wireframes ASCII:
- Tela de login
- Dashboard principal
- Lista de pets
- Histórico de vacinação

**C) Avaliação de Viabilidade**
Para cada ideia, avalio:
- É tecnicamente viável? (tenho conhecimento/tempo?)
- Resolve o problema do usuário?
- Cabe no escopo de 14 semanas?

**D) Seleção das Melhores Ideias**
Ficaram no MVP:
- ✅ Autenticação segura
- ✅ CRUD de pets
- ✅ Registro de vacinas
- ✅ Alertas básicos

Funcionalidades extras (se der tempo):
- ⚪ Geração de PDF
- ⚪ Upload de documentos
- ⚪ Dashboard com gráficos

---

#### FASE 4: PROTOTIPAÇÃO (Quinzenas 6-10)

**Objetivo:** Construir o MVP (Produto Mínimo Viável).

**Abordagem incremental:**
1. **Sprint 1 (Semanas 6-7):** Estrutura base + autenticação
2. **Sprint 2 (Semanas 7-8):** CRUD de pets
3. **Sprint 3 (Semanas 8-9):** Sistema de vacinação
4. **Sprint 4 (Semanas 9-10):** Alertas e refinamentos

**Protótipo de baixa fidelidade (já feito):**
- Wireframes ASCII no documento de requisitos

**Protótipo de alta fidelidade (a fazer):**
- Sistema funcionando com interface Bootstrap
- Banco de dados SQLite operacional
- Funcionalidades essenciais implementadas

**Características do MVP:**
- Funciona end-to-end (usuário consegue usar)
- Interface simples mas funcional
- Dados persistem no banco
- Segurança básica implementada

---

#### FASE 5: TESTE (Quinzenas 11-14)

**Objetivo:** Validar a solução com usuários reais e melhorar.

**Tipos de teste que farei:**

**A) Testes Funcionais**
- Todas as funcionalidades funcionam?
- Há bugs ou erros?
- Performance é aceitável?

**B) Testes de Usabilidade**
- Usuários conseguem usar sem instruções?
- Interface é intuitiva?
- Fluxos fazem sentido?

**C) Testes com Usuários Reais**
- Pedir para 3-5 pessoas usarem o sistema
- Observar dificuldades
- Coletar feedback estruturado:
  - O que gostou?
  - O que não funcionou bem?
  - O que falta?
  - Usaria no dia a dia?

**D) Iteração e Melhoria**
- Corrigir bugs encontrados
- Ajustar interface conforme feedback
- Adicionar pequenas melhorias
- Documentar aprendizados

**Resultado final:**
- Sistema validado por usuários reais ✓
- Documentação completa (técnica + usuário) ✓
- Apresentação final com aprendizados ✓

---

### 2.3 Design Thinking vs Abordagem Tradicional

**Abordagem Tradicional (Waterfall):**
1. Levantamento de requisitos
2. Projeto/design completo
3. Implementação total
4. Testes finais
5. Entrega

**Problema:** Se descobrir que usuário não gosta, já gastou muito tempo/dinheiro.

**Design Thinking (Iterativo):**
1. Entende usuário
2. Define problema
3. Protótipo rápido
4. Testa com usuário
5. Aprende e ajusta
6. Repete o ciclo

**Vantagem:** Valida cedo, reduz risco de fazer algo inútil.

**No meu projeto:**
- ✅ Não vou passar 14 semanas codificando para só no final descobrir que não serve
- ✅ Entrevistas na semana 2 já me darão direção
- ✅ MVP em 5 semanas, depois testes e ajustes
- ✅ Se algo não funcionar, pivoto rapidamente

---

## 3. ENGENHARIA DE SOFTWARE

### 3.1 Análise de Requisitos

**O que são requisitos:**
São descrições do que o sistema deve fazer (funcionais) e como deve se comportar (não-funcionais).

**Técnicas que usei:**

**A) Requisitos Funcionais (RF)**
Descrevi 19 funcionalidades específicas:

**Exemplos:**
- **RF01 - Cadastro de Usuário**
  - O sistema deve permitir que usuários criem conta com nome, email, senha
  - Validações: email único, senha mínima 8 caracteres
  - Resultado: usuário criado e redirecionado para login

- **RF05 - Cadastrar Pet**
  - Usuário autenticado pode cadastrar pet com: nome, espécie, raça, data nascimento
  - Um usuário pode ter N pets
  - Resultado: pet salvo e exibido na lista

- **RF10 - Registrar Vacina**
  - Para cada pet, registrar: nome vacina, data aplicação, lote, próxima dose
  - Resultado: vacina registrada no histórico

**B) Requisitos Não-Funcionais (RNF)**
Descrevi 12 características de qualidade:

**Exemplos:**
- **RNF01 - Usabilidade**
  - Interface responsiva (funciona em mobile, tablet, desktop)
  - Tempo de aprendizado < 10 minutos
  - Linguagem simples, sem jargões técnicos

- **RNF04 - Segurança**
  - Senhas armazenadas com hash bcrypt
  - Proteção contra SQL Injection (uso de ORM)
  - Sessões com timeout de 30 minutos
  - HTTPS em produção

- **RNF06 - Performance**
  - Tempo de resposta < 2 segundos
  - Suporta 100 usuários simultâneos
  - Otimização de queries no banco

**C) Casos de Uso**
Descrevi 3 casos de uso completos com fluxos:

**Exemplo: UC01 - Gerenciar Vacinas**
- **Ator:** Usuário autenticado
- **Pré-condição:** Ter pelo menos 1 pet cadastrado
- **Fluxo Principal:**
  1. Usuário acessa "Meus Pets"
  2. Seleciona um pet
  3. Clica em "Adicionar Vacina"
  4. Preenche formulário (nome, data, próxima dose)
  5. Sistema valida e salva
  6. Exibe histórico atualizado
- **Fluxo Alternativo:** Se data inválida, exibe erro e solicita correção
- **Pós-condição:** Vacina registrada no banco e visível no histórico

---

### 3.2 Modelagem de Dados

**Técnicas de Modelagem:**

**A) Diagrama Entidade-Relacionamento (ER)**
Criei modelo com 3 entidades principais:

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│  USUARIO    │         │     PET     │         │   VACINA    │
├─────────────┤         ├─────────────┤         ├─────────────┤
│ id (PK)     │────1:N──│ id (PK)     │────1:N──│ id (PK)     │
│ nome        │         │ usuario_id  │         │ pet_id (FK) │
│ email       │         │ nome        │         │ nome        │
│ senha_hash  │         │ especie     │         │ data_aplic  │
│ data_cad    │         │ raca        │         │ lote        │
└─────────────┘         │ data_nasc   │         │ prox_dose   │
                        │ data_cad    │         │ observacoes │
                        └─────────────┘         └─────────────┘
```

**Relacionamentos:**
- 1 Usuário pode ter N Pets (1:N)
- 1 Pet pode ter N Vacinas (1:N)
- **Cascata:** Se excluir Pet, exclui suas Vacinas

**B) Normalização**
Apliquei até 3ª Forma Normal:

- **1FN:** Todos os campos são atômicos (não há listas em colunas)
- **2FN:** Não há dependências parciais (cada tabela tem chave única)
- **3FN:** Não há dependências transitivas (dados não se repetem)

**Exemplo de normalização:**
❌ **Errado (não normalizado):**
```
Pet: [id, nome, usuario_nome, usuario_email, vacinas]
```
Problema: Dados do usuário repetem para cada pet

✅ **Correto (normalizado):**
```
Usuario: [id, nome, email]
Pet: [id, usuario_id, nome]
Vacina: [id, pet_id, nome, data]
```

**C) Dicionário de Dados**
Para cada campo, documentei:
- Nome
- Tipo de dado
- Tamanho
- Obrigatoriedade
- Restrições
- Descrição

**Exemplo:**
| Campo | Tipo | Tamanho | Obrigatório | Restrições | Descrição |
|-------|------|---------|-------------|------------|-----------|
| email | VARCHAR | 120 | Sim | UNIQUE | Email do usuário para login |
| senha_hash | VARCHAR | 255 | Sim | - | Senha criptografada com bcrypt |
| data_nasc | DATE | - | Não | <= hoje | Data de nascimento do pet |

---

### 3.3 Arquitetura de Software

**Arquitetura em Camadas (4 layers):**

```
┌─────────────────────────────────────────────┐
│  CAMADA DE APRESENTAÇÃO (Frontend)          │
│  - HTML5 + CSS3 + Bootstrap 5               │
│  - Templates Jinja2                         │
│  - JavaScript (validações client-side)      │
└─────────────────────────────────────────────┘
                    ⬇️ HTTP
┌─────────────────────────────────────────────┐
│  CAMADA DE APLICAÇÃO (Controllers)          │
│  - Flask Routes                             │
│  - Validação de formulários                 │
│  - Gerenciamento de sessões                 │
└─────────────────────────────────────────────┘
                    ⬇️
┌─────────────────────────────────────────────┐
│  CAMADA DE NEGÓCIO (Business Logic)         │
│  - Regras de validação                      │
│  - Cálculos (próxima dose, alertas)         │
│  - Lógica de autenticação                   │
└─────────────────────────────────────────────┘
                    ⬇️
┌─────────────────────────────────────────────┐
│  CAMADA DE DADOS (Database)                 │
│  - SQLAlchemy ORM                           │
│  - SQLite / PostgreSQL                      │
│  - Migrations com Flask-Migrate             │
└─────────────────────────────────────────────┘
```

**Vantagens desta arquitetura:**
- ✅ Separação de responsabilidades
- ✅ Facilita testes (posso testar cada camada)
- ✅ Manutenção simplificada
- ✅ Reusabilidade de código

**Padrão MVC (Model-View-Controller):**
Flask usa variação do MVC:
- **Model:** Classes SQLAlchemy (Usuario, Pet, Vacina)
- **View:** Templates HTML com Jinja2
- **Controller:** Routes do Flask (@app.route)

---

### 3.4 Regras de Negócio

Identifiquei 13 regras essenciais:

**Exemplos:**
1. **RN01:** Usuário não pode cadastrar pet sem estar autenticado
2. **RN03:** Data de nascimento do pet não pode ser futura
3. **RN05:** Email deve ser único no sistema (não permite duplicatas)
4. **RN07:** Vacina só pode ser registrada para pet existente do usuário
5. **RN09:** Alerta é gerado 30 dias antes da próxima dose
6. **RN12:** Senha deve ter mínimo 8 caracteres com letras e números

**Como implementarei:**
- Validações no backend (Flask-WTF)
- Validações no banco (constraints)
- Validações na camada de negócio (métodos das classes)

---

### 3.5 Testes de Software

**Tipos de teste que farei:**

**A) Testes Unitários**
Testar funções isoladas:
```python
def test_usuario_senha_invalida():
    # Testa se senha < 8 chars é rejeitada
    assert validar_senha("abc123") == False
    assert validar_senha("abc12345") == True
```

**B) Testes de Integração**
Testar fluxos completos:
```python
def test_criar_pet_e_vacina():
    # 1. Criar usuário
    # 2. Fazer login
    # 3. Criar pet
    # 4. Adicionar vacina
    # 5. Verificar que vacina aparece no histórico
```

**C) Testes de Interface (Manuais)**
- Testar em diferentes navegadores (Chrome, Firefox)
- Testar em diferentes dispositivos (mobile, tablet, desktop)
- Verificar responsividade

**Ferramentas:**
- `pytest` para testes automatizados
- `coverage` para medir cobertura de testes
- Objetivo: > 80% de cobertura

---

## 4. TECNOLOGIAS WEB

### 4.1 Flask Framework

**O que é Flask:**
Flask é um micro-framework web em Python. "Micro" não significa limitado, mas sim que mantém o núcleo simples e extensível.

**Por que escolhi Flask (vs Django):**

| Critério | Flask | Django | Escolha |
|----------|-------|--------|---------|
| Curva de aprendizado | Suave | Íngreme | ✅ Flask |
| Escopo do projeto | Pequeno/Médio | Médio/Grande | ✅ Flask |
| Tempo disponível | 14 semanas | Precisa mais | ✅ Flask |
| Flexibilidade | Alta | Opiniático | ✅ Flask |
| Admin pronto | Não | Sim | Django |

**Conceitos fundamentais do Flask:**

**A) Rotas (Routes)**
```python
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pets/<int:id>')
def ver_pet(id):
    pet = Pet.query.get(id)
    return render_template('pet.html', pet=pet)
```

**B) Templates (Jinja2)**
```html
<!-- pets.html -->
<h1>Pets de {{ usuario.nome }}</h1>
{% for pet in pets %}
  <div class="card">
    <h3>{{ pet.nome }}</h3>
    <p>{{ pet.especie }} - {{ pet.raca }}</p>
  </div>
{% endfor %}
```

**C) Formulários (Flask-WTF)**
```python
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')
```

**D) Sessões e Autenticação (Flask-Login)**
```python
@login_required
def meus_pets():
    # Apenas usuários logados acessam
    pets = current_user.pets
    return render_template('meus_pets.html', pets=pets)
```

**Extensões que usarei:**
- `Flask-SQLAlchemy`: ORM para banco de dados
- `Flask-Login`: Gerenciamento de sessões
- `Flask-WTF`: Formulários com validação
- `Flask-Migrate`: Migrations do banco
- `Flask-Bcrypt`: Hash de senhas

---

### 4.2 HTML5 e CSS3

**HTML5 - Estrutura Semântica:**
Uso tags semânticas para melhor estrutura:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carteira Pet Digital</title>
</head>
<body>
    <header>
        <nav><!-- Menu --></nav>
    </header>
    
    <main>
        <section id="dashboard">
            <h1>Meus Pets</h1>
            <article class="pet-card">
                <!-- Conteúdo -->
            </article>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 Carteira Pet Digital</p>
    </footer>
</body>
</html>
```

**CSS3 - Estilização:**
Conceitos que aplicarei:
- **Box Model:** margin, padding, border
- **Flexbox:** Layout responsivo
- **Grid:** Organização de cards
- **Media Queries:** Adaptação mobile

```css
/* Mobile First */
.pet-card {
    width: 100%;
    padding: 1rem;
}

/* Tablet */
@media (min-width: 768px) {
    .pet-card {
        width: 48%;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .pet-card {
        width: 30%;
    }
}
```

---

### 4.3 Bootstrap 5

**O que é Bootstrap:**
Framework CSS que fornece componentes prontos e sistema de grid responsivo.

**Por que usar Bootstrap:**
- ✅ Acelera desenvolvimento (não preciso criar tudo do zero)
- ✅ Responsivo por padrão (mobile-first)
- ✅ Consistência visual automática
- ✅ Componentes testados e documentados

**Componentes que usarei:**

**A) Grid System**
```html
<div class="container">
    <div class="row">
        <div class="col-md-4">Pet 1</div>
        <div class="col-md-4">Pet 2</div>
        <div class="col-md-4">Pet 3</div>
    </div>
</div>
```

**B) Cards**
```html
<div class="card">
    <div class="card-header">Thor - Cachorro</div>
    <div class="card-body">
        <p>Raça: Golden Retriever</p>
        <p>Nascimento: 15/03/2020</p>
        <a href="#" class="btn btn-primary">Ver Vacinas</a>
    </div>
</div>
```

**C) Formulários**
```html
<form method="POST">
    <div class="mb-3">
        <label for="nome" class="form-label">Nome do Pet</label>
        <input type="text" class="form-control" id="nome" name="nome">
    </div>
    <button type="submit" class="btn btn-success">Cadastrar</button>
</form>
```

**D) Navbar**
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">Carteira Pet</a>
    <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link" href="/pets">Meus Pets</a></li>
        <li class="nav-item"><a class="nav-link" href="/logout">Sair</a></li>
    </ul>
</nav>
```

**E) Alertas**
```html
<div class="alert alert-warning" role="alert">
    ⚠️ A vacina antirrábica do Thor vence em 5 dias!
</div>
```

---

### 4.4 JavaScript (Básico)

**Uso limitado mas importante:**

**A) Validações Client-Side**
```javascript
function validarFormulario() {
    let nome = document.getElementById('nome').value;
    if (nome.length < 2) {
        alert('Nome deve ter pelo menos 2 caracteres');
        return false;
    }
    return true;
}
```

**B) Interatividade**
```javascript
// Confirmar exclusão
function confirmarExclusao(nomePet) {
    return confirm(`Tem certeza que deseja excluir ${nomePet}?`);
}
```

**C) Máscaras de Data**
Usar biblioteca Inputmask para formatar datas automaticamente.

**Filosofia:** Usar JavaScript apenas quando necessário, deixar lógica principal no backend.

---

## 5. BANCO DE DADOS

### 5.1 Conceitos Fundamentais

**O que é um Banco de Dados:**
Sistema organizado para armazenar, gerenciar e recuperar informações de forma eficiente.

**Tipos de Banco de Dados:**

| Tipo | Exemplo | Uso | Minha escolha |
|------|---------|-----|---------------|
| Relacional (SQL) | PostgreSQL, MySQL, SQLite | Dados estruturados | ✅ Sim |
| NoSQL | MongoDB | Dados não estruturados | Não |
| Chave-Valor | Redis | Cache | Não |

**Por que Relacional:**
- ✅ Dados têm estrutura clara (usuários, pets, vacinas)
- ✅ Relacionamentos bem definidos (1:N)
- ✅ ACID (Atomicidade, Consistência, Isolamento, Durabilidade)
- ✅ Já conheço SQL

---

### 5.2 SQLite vs PostgreSQL

**Estratégia Híbrida:**

**SQLite (Desenvolvimento):**
- Arquivo único (pet_carteira.db)
- Sem necessidade de servidor
- Fácil de configurar
- Perfeito para testar localmente

**PostgreSQL (Produção - se hospedar):**
- Mais robusto
- Melhor performance com muitos usuários
- Recursos avançados (full-text search)
- Suportado por Heroku, Railway, etc.

**Migração fácil:**
Com SQLAlchemy, trocar de SQLite para PostgreSQL é mudar 1 linha de configuração!

```python
# Desenvolvimento
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet_carteira.db'

# Produção
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@host/db'
```

---

### 5.3 SQL - Structured Query Language

**Comandos básicos que usarei:**

**A) DDL (Data Definition Language) - Estrutura**

**Criar tabelas:**
```sql
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    nome VARCHAR(50) NOT NULL,
    especie VARCHAR(30) NOT NULL,
    raca VARCHAR(50),
    data_nascimento DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);

CREATE TABLE vacina (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_id INTEGER NOT NULL,
    nome_vacina VARCHAR(100) NOT NULL,
    data_aplicacao DATE NOT NULL,
    lote VARCHAR(50),
    proxima_dose DATE,
    observacoes TEXT,
    FOREIGN KEY (pet_id) REFERENCES pet(id) ON DELETE CASCADE
);
```

**B) DML (Data Manipulation Language) - Dados**

**Inserir:**
```sql
INSERT INTO pet (usuario_id, nome, especie, raca, data_nascimento)
VALUES (1, 'Thor', 'Cachorro', 'Golden Retriever', '2020-03-15');
```

**Consultar:**
```sql
-- Buscar pets de um usuário
SELECT * FROM pet WHERE usuario_id = 1;

-- Buscar vacinas de um pet com próxima dose próxima
SELECT * FROM vacina 
WHERE pet_id = 5 
AND proxima_dose BETWEEN '2026-03-01' AND '2026-03-31';

-- JOIN: Buscar todos os pets e seus donos
SELECT u.nome as dono, p.nome as pet, p.especie
FROM usuario u
INNER JOIN pet p ON u.id = p.usuario_id;
```

**Atualizar:**
```sql
UPDATE pet 
SET nome = 'Thor da Silva' 
WHERE id = 1;
```

**Deletar:**
```sql
DELETE FROM vacina WHERE id = 10;
```

**C) DQL (Consultas Avançadas)**

**Agregações:**
```sql
-- Contar quantos pets cada usuário tem
SELECT u.nome, COUNT(p.id) as total_pets
FROM usuario u
LEFT JOIN pet p ON u.id = p.usuario_id
GROUP BY u.id;

-- Listar vacinas que vencem nos próximos 30 dias
SELECT p.nome as pet, v.nome_vacina, v.proxima_dose
FROM pet p
INNER JOIN vacina v ON p.id = v.pet_id
WHERE v.proxima_dose BETWEEN CURRENT_DATE AND DATE(CURRENT_DATE, '+30 days')
ORDER BY v.proxima_dose;
```

---

### 5.4 ORM - SQLAlchemy

**O que é ORM (Object-Relational Mapping):**
Camada que traduz objetos Python em tabelas SQL automaticamente.

**Vantagem:**
- Escrevo Python, não SQL direto
- Proteção contra SQL Injection
- Facilita troca de banco de dados
- Código mais limpo e legível

**Modelos SQLAlchemy:**

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamento
    pets = db.relationship('Pet', backref='dono', lazy=True, cascade='all, delete-orphan')

class Pet(db.Model):
    __tablename__ = 'pet'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    especie = db.Column(db.String(30), nullable=False)
    raca = db.Column(db.String(50))
    data_nascimento = db.Column(db.Date)
    
    # Relacionamento
    vacinas = db.relationship('Vacina', backref='pet', lazy=True, cascade='all, delete-orphan')

class Vacina(db.Model):
    __tablename__ = 'vacina'
    
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    nome_vacina = db.Column(db.String(100), nullable=False)
    data_aplicacao = db.Column(db.Date, nullable=False)
    lote = db.Column(db.String(50))
    proxima_dose = db.Column(db.Date)
    observacoes = db.Column(db.Text)
```

**Operações com ORM:**

**Criar:**
```python
novo_pet = Pet(
    usuario_id=1,
    nome='Thor',
    especie='Cachorro',
    raca='Golden Retriever'
)
db.session.add(novo_pet)
db.session.commit()
```

**Consultar:**
```python
# Buscar por ID
pet = Pet.query.get(5)

# Buscar por filtro
pets = Pet.query.filter_by(usuario_id=1).all()

# Buscar um
pet = Pet.query.filter_by(nome='Thor').first()

# Buscar com JOIN automático
usuario = Usuario.query.get(1)
pets_do_usuario = usuario.pets  # Acessa relacionamento
```

**Atualizar:**
```python
pet = Pet.query.get(1)
pet.nome = 'Thor da Silva'
db.session.commit()
```

**Deletar:**
```python
pet = Pet.query.get(1)
db.session.delete(pet)
db.session.commit()  # Vacinas deletadas automaticamente (cascade)
```

---

### 5.5 Migrations (Flask-Migrate)

**O que são Migrations:**
Versionamento do esquema do banco de dados. Como Git, mas para estrutura de tabelas.

**Fluxo:**
```bash
# Inicializar
flask db init

# Criar migration (quando altero models)
flask db migrate -m "Adiciona tabela de vacinas"

# Aplicar migration
flask db upgrade

# Reverter (se necessário)
flask db downgrade
```

**Vantagem:**
- Histórico de mudanças no BD
- Facilita deploy (rodar upgrade em produção)
- Permite reverter alterações

---

## 6. CONTROLE DE VERSÃO

### 6.1 Git - Conceitos Fundamentais

**O que é Git:**
Sistema de controle de versão distribuído. Cada desenvolvedor tem cópia completa do histórico.

**Por que usar:**
- ✅ Histórico completo de mudanças
- ✅ Possibilidade de reverter alterações
- ✅ Trabalho em branches (funcionalidades isoladas)
- ✅ Colaboração facilitada
- ✅ Backup automático (quando push para GitHub)

**Conceitos essenciais:**

**A) Repository (Repositório)**
Pasta do projeto versionada pelo Git.

**B) Commit**
"Foto" do estado do projeto em determinado momento.
```bash
git commit -m "Adiciona modelo de Pet e tela de cadastro"
```

**C) Branch**
Linha de desenvolvimento paralela.
```
main ──●──●──●──●
        \
         └─●──●  feature/alertas
```

**D) Stage (Área de preparação)**
```bash
git add models.py       # Adiciona arquivo à stage
git status              # Vê o que está staged
git commit -m "Mensagem"  # Commita o que está staged
```

**E) Push/Pull**
```bash
git push origin main    # Envia commits para GitHub
git pull origin main    # Baixa commits do GitHub
```

---

### 6.2 Fluxo de Trabalho Git

**Meu fluxo típico:**

```bash
# 1. Criar feature branch
git checkout -b feature/cadastro-vacinas

# 2. Fazer alterações no código
# ... editar arquivos ...

# 3. Ver o que mudou
git status
git diff

# 4. Adicionar arquivos
git add app/routes/vacinas.py
git add app/templates/vacinas.html

# 5. Commitar
git commit -m "Implementa cadastro de vacinas com validação"

# 6. Mais alterações, mais commits...
git add app/models.py
git commit -m "Adiciona relacionamento Pet-Vacina"

# 7. Enviar para GitHub
git push origin feature/cadastro-vacinas

# 8. Mesclar com main (depois de testar)
git checkout main
git merge feature/cadastro-vacinas
git push origin main

# 9. Deletar branch feature (opcional)
git branch -d feature/cadastro-vacinas
```

---

### 6.3 Boas Práticas de Commits

**Mensagens descritivas:**

❌ **Ruim:**
```
git commit -m "fix"
git commit -m "mudanças"
git commit -m "atualizei"
```

✅ **Bom:**
```
git commit -m "Corrige validação de email no formulário de cadastro"
git commit -m "Adiciona campo 'lote' na tabela de vacinas"
git commit -m "Implementa sistema de alertas com cron job"
```

**Formato que seguirei:**
```
<tipo>: <descrição curta>

<descrição detalhada opcional>

Co-Authored-By: Oz <oz-agent@warp.dev>
```

**Tipos:**
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação (não afeta código)
- `refactor:` Refatoração
- `test:` Testes
- `chore:` Tarefas de manutenção

---

### 6.4 GitHub

**O que é GitHub:**
Plataforma de hospedagem de repositórios Git com features extras (issues, pull requests, etc.).

**Estrutura do meu repositório:**

```
carteira-pet-digital/
├── README.md              # Documentação principal
├── .gitignore             # Arquivos a ignorar
├── requirements.txt       # Dependências Python
├── config.py              # Configurações
├── run.py                 # Arquivo para rodar app
├── docs/                  # Documentação extra
│   ├── Analise_Requisitos.md
│   ├── Wireframes/
│   └── Diagramas/
├── app/                   # Código da aplicação
│   ├── __init__.py
│   ├── models.py          # Modelos SQLAlchemy
│   ├── routes/            # Rotas (controllers)
│   ├── templates/         # HTML
│   ├── static/            # CSS, JS, imagens
│   └── utils.py           # Funções auxiliares
├── tests/                 # Testes automatizados
│   ├── test_models.py
│   └── test_routes.py
└── migrations/            # Migrations do banco
```

**README.md (estrutura):**
```markdown
# Carteira Digital de Vacinação para PET

Descrição do projeto...

## Tecnologias
- Python 3.x
- Flask
- SQLite
- Bootstrap 5

## Instalação
```bash
pip install -r requirements.txt
flask db upgrade
flask run
```

## Autor
[Seu Nome] - Engenharia de Computação UNIVESP
```

**`.gitignore` (não commitar):**
```
# Virtual environment
venv/
env/

# Database
*.db
*.sqlite

# Python cache
__pycache__/
*.pyc

# Secrets
.env
config_secret.py

# IDE
.vscode/
.idea/
```

---

### 6.5 Commits Mínimos Exigidos (Quinzena 1)

A disciplina exige **pelo menos 3 commits significativos**:

**Minha estratégia:**

**Commit 1:** Estrutura inicial
```bash
git add README.md .gitignore
git commit -m "docs: Inicializa repositório com README e estrutura de pastas

Co-Authored-By: Oz <oz-agent@warp.dev>"
```

**Commit 2:** Documentação
```bash
git add docs/Analise_Requisitos.md docs/Wireframes/
git commit -m "docs: Adiciona análise de requisitos e wireframes iniciais

Inclui:
- 19 requisitos funcionais
- 12 requisitos não-funcionais
- Diagrama ER
- 4 wireframes ASCII

Co-Authored-By: Oz <oz-agent@warp.dev>"
```

**Commit 3:** Configuração técnica
```bash
git add requirements.txt config.py app/__init__.py
git commit -m "chore: Configura ambiente Flask e dependências

- Flask 3.0
- SQLAlchemy
- Flask-Login
- Flask-WTF
- Bootstrap 5

Co-Authored-By: Oz <oz-agent@warp.dev>"
```

---

## 7. GESTÃO DE PROJETOS

### 7.1 Cronograma (14 Semanas)

Planejei o projeto seguindo as quinzenas:

| Quinzena | Semanas | Fase Design Thinking | Entregas |
|----------|---------|---------------------|----------|
| **Q1** | 1-2 | Empatia | Plano de Ação + GitHub |
| **Q2** | 3-4 | Definição | Personas + Problema definido |
| **Q3** | 5-6 | Ideação | Wireframes + Backlog |
| **Q4** | 7-8 | Prototipação (Sprint 1-2) | Auth + CRUD Pets |
| **Q5** | 9-10 | Prototipação (Sprint 3-4) | Vacinas + Alertas |
| **Q6** | 11-12 | Teste | Testes com usuários |
| **Q7** | 13-14 | Refinamento | Apresentação final |

**Detalhamento Quinzena 1 (onde estamos):**

**Semana 1:**
- Dia 1-2: Configurar ambiente (Python, Git, VS Code)
- Dia 3-4: Criar repositório e estrutura
- Dia 5-6: Estudar Flask (tutorial Hello World)
- Dia 7: Documentar e organizar

**Semana 2:**
- Dia 8-9: Entrevistas com donos de pets
- Dia 10-11: Levantamento bibliográfico
- Dia 12-13: Formalizar Plano de Ação
- Dia 14: Revisar e enviar entregas

---

### 7.2 Metodologia Ágil (Adaptada)

**Inspiração em Scrum, adaptado para projeto individual:**

**Sprints de 2 semanas:**
Cada quinzena é uma sprint com:
- **Planning:** Definir o que fazer
- **Daily (mental):** Revisar progresso diário
- **Review:** Mostrar o que fiz
- **Retrospective:** O que aprendi?

**Backlog Priorizado:**

**Prioridade ALTA (MVP):**
- [ ] Autenticação (cadastro, login, logout)
- [ ] CRUD de pets
- [ ] Registro de vacinas
- [ ] Histórico de vacinas
- [ ] Alertas básicos (query manual)

**Prioridade MÉDIA:**
- [ ] Dashboard com estatísticas
- [ ] Filtros e busca
- [ ] Perfil do usuário
- [ ] Alertas automáticos (cron)

**Prioridade BAIXA (extras):**
- [ ] Geração de PDF
- [ ] Upload de documentos
- [ ] Compartilhamento de carteira
- [ ] Integração com clínicas

**Definição de "Pronto" (DoD - Definition of Done):**
Para considerar uma funcionalidade pronta:
- ✅ Código implementado e testado
- ✅ Interface funcional
- ✅ Sem bugs conhecidos
- ✅ Documentação atualizada
- ✅ Commit no Git

---

### 7.3 Gestão de Riscos

Identifiquei 6 riscos principais e mitigações:

| # | Risco | Probabilidade | Impacto | Mitigação |
|---|-------|---------------|---------|-----------|
| **R1** | Falta de tempo (estudo + trabalho) | Alta | Alto | Cronograma realista, MVP bem definido |
| **R2** | Dificuldade técnica com Flask | Média | Médio | Estudar documentação, buscar ajuda em fóruns |
| **R3** | Escopo muito grande | Média | Alto | Priorização rigorosa, foco no MVP |
| **R4** | Problemas com hospedagem | Baixa | Baixo | Funciona local, hospedagem é extra |
| **R5** | Feedback negativo de usuários | Baixa | Médio | Testes em múltiplas iterações |
| **R6** | Perda de dados/código | Baixa | Alto | Commits frequentes, push para GitHub |

**Plano de contingência:**
- Se atrasar, cortar funcionalidades extras (PDF, upload)
- Se Flask muito difícil, simplificar (sem ORM, SQL direto)
- Se não conseguir entrevistar 5 pessoas, entrevistar 3

---

### 7.4 Recursos Necessários

**Recursos Técnicos:**
- ✅ Computador (já tenho)
- ✅ Internet (tenho)
- ✅ Software gratuito:
  - Python (free)
  - VS Code (free)
  - Git (free)
  - GitHub (free)
  - SQLite (free)

**Recursos Humanos:**
- Eu (desenvolvimento)
- 3-5 donos de pets (entrevistas/testes)
- Professor orientador (feedback)

**Recursos Educacionais:**
- Documentações oficiais (Flask, SQLAlchemy, Bootstrap)
- Material da disciplina (UNIVESP)
- Fóruns (Stack Overflow, Reddit)
- YouTube (tutoriais complementares)

**Tempo:**
- 1-2 horas/dia × 7 dias × 14 semanas = 98-196 horas
- Disciplina: 80 horas
- Tenho folga para imprevistos ✓

---

## 8. DOMÍNIO DO PROBLEMA

### 8.1 Contexto Veterinário

**Vacinação Animal - Importância:**

**Saúde do Animal:**
- Previne doenças graves (raiva, cinomose, parvovirose, leptospirose)
- Reduz mortalidade infantil em filhotes
- Aumenta expectativa de vida

**Saúde Pública:**
- Raiva é zoonose (transmite para humanos)
- Leptospirose pode infectar pessoas
- Controle de epidemias

**Calendário Vacinal Típico (Cães):**

**Filhotes:**
- 6-8 semanas: V8 ou V10 (1ª dose)
- 9-11 semanas: V8 ou V10 (2ª dose)
- 12-14 semanas: V8 ou V10 (3ª dose)
- 16 semanas: Antirrábica

**Adultos (reforço anual):**
- V8 ou V10: 1x/ano
- Antirrábica: 1x/ano
- Outras conforme necessidade (gripe canina, giárdia)

**O que é cada vacina:**
- **V8:** Protege contra 8 doenças (cinomose, parvovirose, hepatite, etc.)
- **V10:** V8 + leptospirose (2 variantes)
- **Antirrábica:** Obrigatória por lei, previne raiva

---

### 8.2 Problema Atual (Carteiras de Papel)

**Levantamento de problemas reais:**

**1. Perda/Dano Físico**
- Carteiras de papel se perdem facilmente
- Sujam, rasgam, molham
- Informações ficam ilegíveis com tempo
- Se perder, perde todo histórico

**2. Falta de Alertas**
- Dono precisa lembrar manualmente
- Não há notificações de vacinas próximas
- Risco de atraso nas vacinas

**3. Desorganização (Múltiplos Pets)**
- Cada pet tem carteira separada
- Difícil gerenciar 2, 3, 5 pets
- Carteiras ficam misturadas em casa

**4. Acesso Limitado**
- Só tem acesso quem tem a carteira física
- Em viagens, pode esquecer
- Não consegue compartilhar facilmente (com família, pet sitter)

**5. Informações Incompletas**
- Veterinários às vezes esquecem de preencher
- Letra ilegível
- Falta informações (lote da vacina)

**6. Sem Histórico Agregado**
- Não consegue visualizar histórico completo facilmente
- Não há estatísticas (quantas vacinas já deu)
- Não agrupa por tipo de vacina

---

### 8.3 Solução Proposta (Justificativa Técnica)

**Por que uma aplicação web resolve:**

**1. Persistência e Backup**
- ✅ Dados armazenados em banco de dados seguro
- ✅ Impossível "perder" fisicamente
- ✅ Backup automático (se hospedar em nuvem)

**2. Alertas Automáticos**
- ✅ Sistema calcula datas automaticamente
- ✅ Envia notificações 30 dias antes
- ✅ Dono não precisa lembrar manualmente

**3. Organização Centralizada**
- ✅ Todos os pets em um só lugar
- ✅ Visão agregada (dashboard)
- ✅ Filtros e buscas rápidas

**4. Acesso Universal**
- ✅ Acessa de qualquer lugar (casa, clínica, viagem)
- ✅ Funciona em mobile, tablet, desktop
- ✅ Apenas precisa de internet

**5. Informações Completas**
- ✅ Campos obrigatórios (garante preenchimento)
- ✅ Histórico detalhado (data, lote, obs.)
- ✅ Sem problema de letra ilegível

**6. Histórico Rico**
- ✅ Timeline visual das vacinas
- ✅ Estatísticas (quantas vacinas, quais faltam)
- ✅ Relatórios e exportação (futuramente)

---

### 8.4 Diferenciais da Solução

**Comparado a outras soluções:**

**vs Anotação em Agenda:**
- ✅ Não perde quando troca agenda
- ✅ Alertas automáticos
- ✅ Histórico organizado

**vs Foto da Carteira no Celular:**
- ✅ Dados estruturados (não só imagem)
- ✅ Busca por vacina, data
- ✅ Alertas inteligentes

**vs Planilha Excel:**
- ✅ Interface mais amigável
- ✅ Acesso de qualquer dispositivo
- ✅ Não precisa conhecimento técnico
- ✅ Alertas automáticos

**vs Apps Comerciais Existentes:**
- ✅ Gratuito e open-source
- ✅ Sem anúncios
- ✅ Privacidade (dados não vendidos)
- ✅ Customizável (posso adicionar features)

---

### 8.5 Público-Alvo Detalhado

**Persona Principal: Maria Silva**

**Demografia:**
- Idade: 35 anos
- Profissão: Professora
- Localização: São Paulo, SP
- Estado civil: Casada, 1 filho
- Renda: Classe média

**Tecnologia:**
- Usa smartphone diariamente (WhatsApp, Instagram)
- Conhecimento médio de tecnologia
- Prefere apps simples e intuitivos
- Usa mais mobile que desktop

**Relação com Pets:**
- Tem 2 cachorros: Thor (Golden, 6 anos) e Mel (Vira-lata, 3 anos)
- Considera-os membros da família
- Preocupada com saúde e bem-estar
- Gasta R$ 200-300/mês com pets (ração, veterinário)

**Dores:**
- Já perdeu carteira de vacinação 1 vez (teve que refazer histórico)
- Esqueceu de dar vacina no prazo (atrasou 2 meses)
- Difícil organizar 2 cachorros (2 carteiras, 2 datas)
- Fica ansiosa quando não lembra se vacinou

**Objetivos:**
- Nunca mais perder histórico de vacinas
- Ser avisada automaticamente quando vacina próxima
- Ter histórico completo e organizado
- Acessar de qualquer lugar (principalmente celular)

**Comportamento:**
- Pesquisa sobre saúde animal no Google
- Segue perfis de pets no Instagram
- Participa de grupos de donos de cachorros no Facebook
- Usa apps de banco, delivery, etc.

**O que faria ela usar meu sistema:**
- Interface bonita e simples
- Funciona bem no celular
- Alertas por email (ela checa diariamente)
- Gratuito
- Não precisa instalar (web, acessa pelo navegador)

---

### 8.6 Validação da Viabilidade

**Por que este projeto é viável em 14 semanas:**

**1. Escopo controlado**
- MVP bem definido (4-5 funcionalidades essenciais)
- Sem integrações complexas
- Tecnologias que conheço ou posso aprender rápido

**2. Tecnologias adequadas**
- Flask: documentação excelente, curva de aprendizado suave
- SQLite: zero configuração, perfeito para desenvolvimento
- Bootstrap: acelera muito o frontend

**3. Problema bem definido**
- Não há ambiguidade no que fazer
- Requisitos claros e priorizados
- Casos de uso simples

**4. Dados simples**
- 3 tabelas apenas (Usuario, Pet, Vacina)
- Relacionamentos diretos (1:N)
- Sem necessidade de processamento complexo

**5. Interface direta**
- Formulários básicos (cadastro, login)
- CRUDs padrão (listar, criar, editar, deletar)
- Nada de interações complexas (drag-drop, real-time)

**6. Sem dependências externas**
- Não depende de APIs de terceiros
- Não precisa integração com clínicas (seria complexo)
- Funciona standalone

**Cronograma realista:**
- 2 semanas: Planejamento + design ✓
- 4 semanas: Desenvolvimento (sprint 1-2) ✓
- 4 semanas: Funcionalidades avançadas (sprint 3-4) ✓
- 2 semanas: Testes com usuários ✓
- 2 semanas: Ajustes finais + apresentação ✓

---

## 📊 REFERÊNCIAS BIBLIOGRÁFICAS

### Referências da Disciplina (Material UNIVESP):

1. **CASALE, A.** Aprendizagem baseada em problemas: desenvolvimento de competências para o ensino em Engenharia. São Paulo: UNIVESP, 2013.

2. **CAVALCANTI, C. M. C.** Design Thinking como metodologia de pesquisa para concepção de um ambiente virtual de aprendizagem centrado no usuário. Dissertação (Mestrado) - UFPE, 2015.

3. **GERHARDT, T. E.; SILVEIRA, D. T.** Métodos de pesquisa. Porto Alegre: Editora da UFRGS, 2009.

4. **SOMMERVILLE, I.** Engenharia de Software. 9ª ed. São Paulo: Pearson, 2011.

5. **PRESSMAN, R. S.** Engenharia de Software: uma abordagem profissional. 7ª ed. Porto Alegre: McGraw-Hill, 2011.

### Documentações Técnicas:

6. **PALLETS PROJECT.** Flask Documentation. Disponível em: https://flask.palletsprojects.com/. Acesso em: 01 mar. 2026.

7. **SQLALCHEMY.** SQLAlchemy Documentation. Disponível em: https://www.sqlalchemy.org/. Acesso em: 01 mar. 2026.

8. **BOOTSTRAP.** Bootstrap 5 Documentation. Disponível em: https://getbootstrap.com/. Acesso em: 01 mar. 2026.

### Domínio do Problema:

9. **IBGE - Instituto Brasileiro de Geografia e Estatística.** Pesquisa Nacional de Saúde. População de animais de estimação no Brasil. 2023.

10. **CFMV - Conselho Federal de Medicina Veterinária.** Manual de Vacinação Animal. Brasília, 2022.

11. **MINISTÉRIO DA SAÚDE.** Guia de Vigilância em Saúde: Raiva. Brasília, 2021.

### Design Thinking:

12. **BROWN, T.** Design Thinking: uma metodologia poderosa para decretar o fim das velhas ideias. Rio de Janeiro: Elsevier, 2010.

13. **IDEO.** Design Thinking for Educators. 2nd Edition. 2013. Disponível em: https://designthinking.ideo.com/. Acesso em: 01 mar. 2026.

---

## 🎯 COMO DEMONSTRAR CONHECIMENTO NA REUNIÃO

### Estratégias para Mostrar Domínio:

**1. Use Terminologia Técnica (com explicação)**
❌ "Vou fazer um sistema"
✅ "Vou desenvolver uma aplicação web usando arquitetura MVC, onde o Flask gerencia o backend, SQLAlchemy faz a persistência e Bootstrap cuida da interface responsiva"

**2. Cite Referências**
❌ "Li sobre isso"
✅ "Segundo Cavalcanti (2015), Design Thinking centrado no usuário exige empatia profunda, por isso planejei entrevistar donos de pets"

**3. Justifique Escolhas**
❌ "Escolhi Flask porque sim"
✅ "Escolhi Flask ao invés de Django porque: 1) curva de aprendizado mais suave, 2) escopo do projeto não exige features pesadas do Django como admin pronto, 3) flexibilidade para escolher extensões"

**4. Mostre Pensamento Crítico**
❌ "Vou fazer tudo que pensei"
✅ "Priorizei MVP com 5 funcionalidades essenciais. Geração de PDF e upload de documentos ficam como extras se houver tempo, pois não são críticos para validar a hipótese principal"

**5. Demonstre Organização**
❌ "Vou fazendo conforme dá"
✅ "Estruturei cronograma em 7 sprints de 2 semanas cada, alinhadas com as fases do Design Thinking. Tenho backlog priorizado e Definition of Done clara"

**6. Antecipe Riscos**
❌ [Não menciona problemas]
✅ "Identifiquei 6 riscos, sendo o principal a gestão de tempo. Mitigação: MVP enxuto e cronograma com buffer de 20%"

**7. Conecte Teoria e Prática**
❌ "Aprendi Flask"
✅ "Estou aplicando ABP: identifiquei o problema (carteiras perdidas), agora busco conhecimentos necessários (Flask, ORM) conforme preciso implementar funcionalidades"

---

## ✅ CHECKLIST DE DOMÍNIO

Antes da reunião, garanta que consegue explicar:

### Design Thinking
- [ ] O que é e por que usamos
- [ ] As 5 fases com detalhes
- [ ] Em qual fase estamos e o que fazemos nela
- [ ] Diferença vs abordagem tradicional

### Engenharia de Software
- [ ] Diferença entre RF e RNF com exemplos
- [ ] O que são casos de uso
- [ ] O que é arquitetura em camadas
- [ ] O que são regras de negócio

### Banco de Dados
- [ ] Por que relacional e não NoSQL
- [ ] Explicar seu diagrama ER
- [ ] Diferença entre SQLite e PostgreSQL
- [ ] O que é ORM e vantagens

### Tecnologias Web
- [ ] Por que Flask e não Django
- [ ] O que é MVC
- [ ] Para que serve Bootstrap
- [ ] Como funciona autenticação

### Git
- [ ] O que é commit
- [ ] O que é branch
- [ ] Por que versionamento é importante
- [ ] Estrutura do seu repositório

### Projeto
- [ ] Problema que resolve
- [ ] Quem é o público-alvo (persona)
- [ ] Por que é viável em 14 semanas
- [ ] Quais os principais riscos

---

## 💬 FRASES-CHAVE PARA USAR

**Demonstrar maturidade técnica:**
- "Optei por uma arquitetura em camadas para separar responsabilidades e facilitar testes"
- "Utilizei normalização até 3FN para evitar redundância de dados"
- "Implementarei cascade delete para manter integridade referencial"
- "O uso de ORM previne SQL Injection e facilita migração entre SGBDs"

**Demonstrar pensamento de engenheira:**
- "Avaliei trade-offs entre Flask e Django considerando escopo, tempo e curva de aprendizado"
- "Priorizei MVP para validar hipóteses antes de investir em funcionalidades extras"
- "Estabeleci métricas claras: tempo de resposta < 2s, interface responsiva, > 80% cobertura de testes"

**Demonstrar alinhamento com metodologia:**
- "Seguindo os princípios do Design Thinking, começarei pela fase de empatia entrevistando usuários reais"
- "Aplicando ABP, identifiquei lacunas de conhecimento e buscarei aprendê-las conforme necessário"
- "A abordagem iterativa permite pivotar rapidamente se feedback de usuários indicar necessidade"

---

**BOA SORTE! VOCÊ ESTÁ PREPARADA! 🚀📚**

_Este repertório demonstra domínio profundo de todos os conteúdos da Quinzena 1._

---

_Documento criado em: 01/03/2026_