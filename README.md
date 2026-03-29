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
```bash
pip install -r requirements.txt
```

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
