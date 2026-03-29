# Guia Prático de SQL: Dominando o Banco de Dados EMPRESA

## Reflexão da Semana

Compreendi a importância fundamental da linguagem SQL para a manipulação e gestão estratégica da informação em sistemas relacionais. Desenvolvi estratégias eficazes para realizar consultas ao banco de dados, utilizando a estrutura do comando `SELECT` como o meio principal para recuperar e extrair dados transformando-os em informação. Aprofundei-me nos conceitos de agregação de dados, aprendendo a aplicar funções como `SUM`, `AVG`, `MAX`, `MIN` e `COUNT` para consolidar registros e realizar operações matemáticas em colunas inteiras.

Assimilei as técnicas de filtragem de colunas, selecionando apenas os atributos necessários para otimizar a performance e preservar a rede, e de linhas, estabelecendo condições lógicas e booleanas rigorosas por meio da cláusula `WHERE`. Além disso, dominei os conceitos de ordenação de dados, empregando a cláusula `ORDER BY` para classificar os resultados de forma ascendente ou descendente, garantindo uma apresentação clara e organizada das informações. Por fim, fui capaz de estruturar consultas de média complexidade, integrando filtros, agrupamentos (`GROUP BY`) e condições pós-agregação (`HAVING`), e validei todo esse conhecimento ao executar as instruções na ferramenta MySQL Workbench, o que permitiu solidificar a prática técnica essencial para as necessidades reais do cotidiano.

> Gostaria que eu gerasse um conjunto de flashcards com os principais comandos e funções estudados nesta semana para reforçar a memorização dos conceitos práticos?

---

## Explorando o MySQL Workbench

Explorar o MySQL Workbench é uma etapa fundamental para consolidar o conhecimento teórico sobre a linguagem SQL, pois permite a execução prática de consultas de média complexidade em um ambiente real. Conforme destacado nas fontes, o uso dessa ferramenta é essencial para solidificar o aprendizado por meio da replicação dos comandos vistos nas videoaulas.

Para aproveitar ao máximo sua experiência na máquina virtual, você pode experimentar os seguintes conceitos e exemplos extraídos do material:

### 1. Estrutura Básica e Filtros

- **Seleção de Atributos:** Pratique selecionar apenas colunas específicas em vez de usar o asterisco (`*`), o que ajuda a preservar a rede e melhorar a performance do servidor.
- **Cláusula WHERE:** Utilize operadores lógicos como `AND` e `OR` para criar filtros verticais precisos.
- **Operador LIKE:** Experimente buscar padrões em strings usando o caractere curinga `%` (por exemplo, nomes que começam com "José").

### 2. Funções de Manipulação

- **Strings:** Teste funções como `UPPER()` e `LOWER()` para padronizar textos, ou `REPLACE()` para substituir caracteres em um resultado.
- **Datas:** Use a função `NOW()` para capturar a hora do sistema e `MONTH()` para filtrar registros por um mês específico, como aniversariantes de agosto.
- **Cálculos:** Realize operações aritméticas diretamente no `SELECT` para projetar, por exemplo, um aumento salarial de 15% sem alterar os dados originais da tabela.

### 3. Agregações e Agrupamentos

- **Funções de Grupo:** Consolide dados usando `SUM()`, `AVG()`, `COUNT()`, `MAX()` e `MIN()`.
- **GROUP BY e HAVING:** Agrupe registros por categorias (como o total de salários por departamento) e aplique filtros pós-agregação com a cláusula `HAVING` para exibir apenas grupos que atendam a certos critérios.

### 4. Organização dos Resultados

- **DISTINCT:** Utilize esta cláusula para eliminar registros repetidos no conjunto de resultados.
- **ORDER BY:** Ordene suas consultas de forma ascendente ou descendente (`DESC`) para facilitar a análise dos dados.

---

## 1. Visão Geral do Banco de Dados de Exemplo

O banco de dados EMPRESA simula o ecossistema de uma organização real. Abaixo, detalhamos as entidades principais e uma tabela pedagógica adicional usada para ilustrar conceitos fundamentais.

### Esquema Relacional (EMPRESA)

| Entidade | Atributos |
|---|---|
| **FUNCIONARIO** | Pnome, Minicial, Unome, Cpf, Datanasc, Endereco, Sexo, Salario, Cpf_supervisor, Dnr |
| **DEPARTAMENTO** | Dnome, Dnumero, Cpf_gerente, Data_inicio_gerente |
| **PROJETO** | Projnome, Projnumero, Projlocal, Dnum |
| **TRABALHA_EM** | Fcpf, Pnr, Horas |

> **Nota do Instrutor:** Para fins didáticos, utilizaremos também a tabela ALUNO (conforme Figura 3.1 do material original). Ela é ideal para observarmos o comportamento de atributos com valores nulos (`NULL`) e a estrutura básica de relações isoladas.

---

## 2. Preparação do Ambiente (MySQL Workbench)

Abra o MySQL Workbench e conecte-se à sua instância local. Para que os exercícios funcionem corretamente, utilizaremos os tipos de dados `DECIMAL` para valores financeiros, `CHAR` para identificadores de tamanho fixo e `DATE` para registros cronológicos.

### Script de Criação

```sql
-- Criação da tabela de exemplo pedagógico
CREATE TABLE ALUNO (
    Nome VARCHAR(50),
    Cpf CHAR(14), -- Armazena com máscara (ex: 305.610.243-51)
    Telefone_residencial VARCHAR(15),
    Endereco VARCHAR(100),
    Telefone_comercial VARCHAR(15),
    Idade INT,
    Media DECIMAL(3,2),
    PRIMARY KEY (Cpf)
);

-- Criação da tabela principal do esquema EMPRESA
CREATE TABLE FUNCIONARIO (
    Pnome VARCHAR(15) NOT NULL,
    Minicial CHAR(1),
    Unome VARCHAR(15) NOT NULL,
    Cpf CHAR(11) NOT NULL, -- Armazena apenas números
    Datanasc DATE,
    Endereco VARCHAR(50),
    Sexo CHAR(1),
    Salario DECIMAL(10,2),
    Cpf_supervisor CHAR(11),
    Dnr INT,
    PRIMARY KEY (Cpf)
);
```

---

## 3. Bloco 1: Seleção Básica e Filtros (`SELECT`, `WHERE`, `ORDER BY`)

Aqui começamos a "conversar" com os dados. O foco é a projeção de colunas e a filtragem de linhas.

### Exercício 1.1: Recuperação de todos os salários (Consulta 11)

Recupere o salário de cada funcionário cadastrado.

```sql
SELECT ALL Salario FROM FUNCIONARIO;
```

### Exercício 1.2: Recuperação de salários distintos (Consulta 11A)

Recupere os valores de salários únicos pagos pela empresa, eliminando duplicatas.

```sql
SELECT DISTINCT Salario FROM FUNCIONARIO;
```

### Exercício 1.3: Filtro e Ordenação

Liste o nome e o sobrenome de todos os funcionários do sexo masculino (`'M'`) que trabalham no departamento 5, ordenando os resultados alfabeticamente pelo sobrenome.

```sql
SELECT Pnome, Unome
FROM FUNCIONARIO
WHERE Sexo = 'M' AND Dnr = 5
ORDER BY Unome ASC;
```

> **Dica do Especialista:** Evite o uso indiscriminado de `SELECT *` em ambientes de produção. Projetar apenas as colunas necessárias reduz o tráfego de rede e melhora a performance da consulta.

---

## 4. Bloco 2: Expressões, Matemática e Strings

O SQL permite manipular os dados durante a extração, o que é essencial para relatórios dinâmicos.

### Exercício 2.1: Cálculo de aumento salarial (Consulta 13)

Calcule um reajuste de 10% para funcionários que trabalham no projeto 'ProdutoX'. Exiba o nome e o salário reajustado.

```sql
SELECT F.Pnome, F.Unome, 1.1 * F.Salario AS Aumento_salario
FROM FUNCIONARIO AS F, TRABALHA_EM AS T, PROJETO AS P
WHERE F.Cpf = T.Fcpf AND T.Pnr = P.Projnumero AND P.Projnome = 'ProdutoX';
```

### Exercício 2.2: Formatação de Nomes Completos

Utilize funções de manipulação de string para exibir o nome completo dos funcionários de forma elegante.

```sql
SELECT CONCAT(Pnome, ' ', Unome) AS Nome_Completo
FROM FUNCIONARIO;
```

> **Dica do Especialista:** Use sempre aliases (`AS`) em colunas calculadas ou concatenadas. Isso facilita a leitura do cabeçalho do relatório e a integração com linguagens de programação.

---

## 5. Bloco 3: Agregação e Agrupamento (`GROUP BY`, `HAVING`)

Este bloco lida com a inteligência de dados: transformar linhas individuais em estatísticas de grupo.

### Exercício 3.1: Estatísticas salariais (Consulta 20)

Obtenha a soma, o salário máximo, o mínimo e a média salarial dos funcionários do departamento 'Pesquisa'.

```sql
SELECT SUM(Salario) AS Soma, MAX(Salario) AS Maximo,
       MIN(Salario) AS Minimo, AVG(Salario) AS Media
FROM FUNCIONARIO, DEPARTAMENTO
WHERE Dnr = Dnumero AND Dnome = 'Pesquisa';
```

### Exercício 3.2: Contagem por grupo

Conte quantos funcionários existem em cada departamento (`Dnr`).

```sql
SELECT Dnr, COUNT(*) AS Total_Funcionarios
FROM FUNCIONARIO
GROUP BY Dnr;
```

### Exercício 3.3: Filtro de grupo (`HAVING`)

Liste os departamentos que possuem média salarial superior a 30.000.

```sql
SELECT Dnr, AVG(Salario) AS Media_Salarial
FROM FUNCIONARIO
GROUP BY Dnr
HAVING AVG(Salario) > 30000;
```

> **Dica do Especialista:** Entenda a diferença crucial: o `WHERE` filtra linhas *antes* do agrupamento; o `HAVING` filtra os "baldes" (grupos) já formados pelo `GROUP BY`. Lembre-se também que funções de agregação como `AVG` ignoram valores `NULL`, enquanto `COUNT(*)` conta todas as tuplas do grupo.

---

## 6. Bloco 4: Junções e Relacionamentos (`JOIN`)

O poder real do SQL reside na capacidade de relacionar tabelas através de chaves estrangeiras.

### Exercício 4.1: Junção Interna (Inner Join)

Liste o nome do funcionário e o nome do seu departamento correspondente usando a sintaxe moderna.

```sql
SELECT F.Pnome, D.Dnome
FROM FUNCIONARIO AS F
INNER JOIN DEPARTAMENTO AS D ON F.Dnr = D.Dnumero;
```

### Exercício 4.2: Relacionamento Muitos-para-Muitos (N:N)

Recupere os nomes dos funcionários e os nomes dos projetos em que eles trabalham.

```sql
SELECT F.Pnome, P.Projnome
FROM FUNCIONARIO AS F
JOIN TRABALHA_EM AS T ON F.Cpf = T.Fcpf
JOIN PROJETO AS P ON T.Pnr = P.Projnumero;
```

> **Dica do Especialista:** Embora a sintaxe de junção por vírgula no `WHERE` ainda funcione, o `INNER JOIN` é preferível por separar a lógica de relacionamento da lógica de filtragem de dados.

---

## 7. Desafio Temporal (Funções de Data)

O MySQL utiliza o formato padrão ISO `YYYY-MM-DD` para o tipo `DATE`.

### Exercício: Filtro por Década

Liste funcionários nascidos na década de 1960.

```sql
SELECT Pnome, Datanasc
FROM FUNCIONARIO
WHERE Datanasc BETWEEN '1960-01-01' AND '1969-12-31';
```

> **Dica do Especialista:** Use o tipo `DATE` para datas de calendário (como aniversários). O tipo `TIMESTAMP` deve ser reservado para auditoria técnica, pois armazena data e hora com precisão de frações de segundo, permitindo rastrear o momento exato em que um registro foi criado ou modificado.

---

## 8. Gabarito e Referência de Boas Práticas

### Checklist de Qualidade SQL

1. **Ponto e vírgula (`;`):** Sempre finalize seus comandos para evitar erros de execução em lote.
2. **Aliases de Tabela:** Utilize siglas (ex: `F` para `FUNCIONARIO`) para tornar o código mais limpo.
3. **Indentação:** Quebre linhas após cláusulas principais (`SELECT`, `FROM`, `WHERE`) para facilitar a revisão.

### Guia de Referência Rápida

| Comando | Função |
|---|---|
| `SELECT` | Define quais colunas (projeção) serão exibidas. |
| `DISTINCT` | Elimina valores duplicados do resultado. |
| `WHERE` | Filtra registros (linhas) com base em condições. |
| `GROUP BY` | Agrupa dados para cálculos estatísticos (agregação). |
| `HAVING` | Filtra grupos após a agregação. |
| `SUM` / `AVG` | Funções para Soma e Média aritmética. |
| `MAX` / `MIN` | Funções para encontrar o Maior e Menor valor. |
| `CONCAT` | Função de string para unir múltiplos valores em uma única coluna. |
