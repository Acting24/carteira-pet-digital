# ==========================================
# SCRIPT DE CONFIGURAÇÃO GIT
# Carteira Digital Pet - PJI110 UNIVESP
# ==========================================

Write-Host "🚀 Configurando repositório Git..." -ForegroundColor Green
Write-Host ""

# Verificar se Git está instalado
try {
    $gitVersion = git --version
    Write-Host "✅ Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git não instalado!" -ForegroundColor Red
    Write-Host "Por favor, instale o Git em: https://git-scm.com/downloads" -ForegroundColor Yellow
    Write-Host "Reinicie o PowerShell após a instalação e execute este script novamente." -ForegroundColor Yellow
    Read-Host "Pressione Enter para sair"
    exit 1
}

Write-Host ""

# Solicitar configurações do usuário
Write-Host "🔧 Configuração do Git" -ForegroundColor Cyan
$userName = Read-Host "Digite seu nome completo"
$userEmail = Read-Host "Digite seu email"

# Configurar Git globalmente
Write-Host ""
Write-Host "⚙️ Configurando Git..." -ForegroundColor Yellow
git config --global user.name "$userName"
git config --global user.email "$userEmail"

Write-Host "✅ Configuração do Git concluída!" -ForegroundColor Green

# Verificar se já é um repositório Git
if (Test-Path ".git") {
    Write-Host "⚠️ Repositório Git já existe nesta pasta!" -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "📁 Inicializando repositório Git..." -ForegroundColor Yellow
    git init
    Write-Host "✅ Repositório Git inicializado!" -ForegroundColor Green
}

# Verificar status
Write-Host ""
Write-Host "📊 Status do repositório:" -ForegroundColor Cyan
git status

# Adicionar todos os arquivos
Write-Host ""
Write-Host "➕ Adicionando arquivos ao Git..." -ForegroundColor Yellow
git add .

# Fazer primeiro commit
Write-Host ""
Write-Host "💾 Fazendo primeiro commit..." -ForegroundColor Yellow
git commit -m "feat: estrutura inicial do projeto Carteira Digital Pet

- Implementação principal em Django baseada no esquema SQL
- Estrutura Flask como alternativa  
- Modelos que replicam tabelas: usuario, tutor, pet, especie, veterinario, vacina
- Documentação completa (README.md + GUIA_DE_UTILIZACAO.md)
- Estrutura de pastas conforme especificações da Quinzena 1
- Templates responsivos com Bootstrap 5
- Configurações prontas para equipe de 7 integrantes

PJI110 - UNIVESP 2026
Co-Authored-By: Oz <oz-agent@warp.dev>"

Write-Host "✅ Primeiro commit realizado!" -ForegroundColor Green

# Mostrar próximos passos
Write-Host ""
Write-Host "🎯 PRÓXIMOS PASSOS:" -ForegroundColor Cyan
Write-Host "1. Criar repositório no GitHub com nome: carteira-pet-digital" -ForegroundColor White
Write-Host "2. Copiar a URL do repositório GitHub" -ForegroundColor White
Write-Host "3. Executar: git remote add origin https://github.com/[usuario]/carteira-pet-digital.git" -ForegroundColor White
Write-Host "4. Executar: git branch -M main" -ForegroundColor White
Write-Host "5. Executar: git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "📚 Consulte o GUIA_DE_UTILIZACAO.md para instruções detalhadas!" -ForegroundColor Yellow
Write-Host ""

Read-Host "Pressione Enter para finalizar"