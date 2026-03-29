# ==========================================
# SCRIPT PARA CONECTAR AO GITHUB  
# Carteira Digital Pet - PJI110 UNIVESP
# ==========================================

Write-Host "🔗 Conectando ao GitHub..." -ForegroundColor Green
Write-Host ""

# Verificar se Git está configurado
try {
    $userName = git config --global user.name
    $userEmail = git config --global user.email
    
    if (-not $userName -or -not $userEmail) {
        Write-Host "❌ Git não está configurado!" -ForegroundColor Red
        Write-Host "Execute primeiro: .\setup_git.ps1" -ForegroundColor Yellow
        Read-Host "Pressione Enter para sair"
        exit 1
    }
    
    Write-Host "✅ Git configurado para: $userName ($userEmail)" -ForegroundColor Green
} catch {
    Write-Host "❌ Git não encontrado!" -ForegroundColor Red
    Write-Host "Instale o Git em: https://git-scm.com/downloads" -ForegroundColor Yellow
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Verificar se é um repositório Git
if (-not (Test-Path ".git")) {
    Write-Host "❌ Esta pasta não é um repositório Git!" -ForegroundColor Red
    Write-Host "Execute primeiro: .\setup_git.ps1" -ForegroundColor Yellow
    Read-Host "Pressione Enter para sair"
    exit 1
}

Write-Host ""
Write-Host "📋 INSTRUÇÕES PARA CRIAR REPOSITÓRIO NO GITHUB:" -ForegroundColor Cyan
Write-Host "1. Acesse: https://github.com" -ForegroundColor White
Write-Host "2. Clique em 'New repository' (botão verde)" -ForegroundColor White  
Write-Host "3. Nome do repositório: carteira-pet-digital" -ForegroundColor Yellow
Write-Host "4. Descrição: Sistema web para gerenciamento de vacinação de pets - PJI110 UNIVESP" -ForegroundColor White
Write-Host "5. Marque como PUBLIC (público)" -ForegroundColor White
Write-Host "6. NÃO marque 'Add a README file' (já temos)" -ForegroundColor White
Write-Host "7. NÃO marque 'Add .gitignore' (já temos)" -ForegroundColor White
Write-Host "8. Clique em 'Create repository'" -ForegroundColor White
Write-Host ""

# Solicitar URL do repositório
$repoUrl = Read-Host "Cole a URL do repositório GitHub que você criou (ex: https://github.com/usuario/carteira-pet-digital.git)"

if (-not $repoUrl) {
    Write-Host "❌ URL do repositório é obrigatória!" -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Verificar se já tem origin configurado
try {
    $existingOrigin = git remote get-url origin 2>$null
    if ($existingOrigin) {
        Write-Host "⚠️ Remote 'origin' já existe: $existingOrigin" -ForegroundColor Yellow
        $overwrite = Read-Host "Deseja sobrescrever? (s/n)"
        if ($overwrite -eq "s" -or $overwrite -eq "S") {
            git remote remove origin
            Write-Host "✅ Remote antigo removido" -ForegroundColor Green
        } else {
            Write-Host "❌ Operação cancelada" -ForegroundColor Red
            Read-Host "Pressione Enter para sair"
            exit 1
        }
    }
} catch {
    # Origin não existe, tudo bem
}

# Conectar ao repositório remoto
Write-Host ""
Write-Host "🔗 Conectando ao repositório GitHub..." -ForegroundColor Yellow
try {
    git remote add origin $repoUrl
    Write-Host "✅ Remote 'origin' configurado!" -ForegroundColor Green
} catch {
    Write-Host "❌ Erro ao configurar remote!" -ForegroundColor Red
    Write-Host $Error[0] -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Configurar branch principal
Write-Host ""
Write-Host "🌿 Configurando branch principal..." -ForegroundColor Yellow
try {
    git branch -M main
    Write-Host "✅ Branch principal configurada como 'main'" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Aviso: Não foi possível renomear branch" -ForegroundColor Yellow
}

# Fazer push inicial
Write-Host ""
Write-Host "⬆️ Enviando arquivos para GitHub..." -ForegroundColor Yellow
Write-Host "Isso pode demorar alguns minutos..." -ForegroundColor Gray

try {
    git push -u origin main
    Write-Host ""
    Write-Host "🎉 SUCESSO! Repositório enviado para GitHub!" -ForegroundColor Green
} catch {
    Write-Host ""
    Write-Host "❌ Erro ao fazer push!" -ForegroundColor Red
    Write-Host "Possíveis soluções:" -ForegroundColor Yellow
    Write-Host "1. Verifique se a URL está correta" -ForegroundColor White
    Write-Host "2. Verifique se o repositório no GitHub está vazio" -ForegroundColor White
    Write-Host "3. Tente fazer login no Git: git config --global credential.helper store" -ForegroundColor White
    Write-Host ""
    Write-Host "Comando para tentar novamente:" -ForegroundColor Cyan
    Write-Host "git push -u origin main" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Pressione Enter para continuar"
}

# Mostrar informações do repositório
Write-Host ""
Write-Host "📋 INFORMAÇÕES DO REPOSITÓRIO:" -ForegroundColor Cyan
Write-Host "URL: $repoUrl" -ForegroundColor White
Write-Host "Branch: main" -ForegroundColor White

try {
    $commitCount = git rev-list --count HEAD
    Write-Host "Commits: $commitCount" -ForegroundColor White
} catch {
    Write-Host "Commits: 1 (estimado)" -ForegroundColor White
}

# Próximos passos
Write-Host ""
Write-Host "🎯 PRÓXIMOS PASSOS:" -ForegroundColor Cyan
Write-Host "1. ✅ Repositório criado e enviado!" -ForegroundColor Green
Write-Host "2. 📋 Adicionar colaboradores:" -ForegroundColor White
Write-Host "   - No GitHub, vá em Settings > Collaborators" -ForegroundColor Gray
Write-Host "   - Clique em 'Add people'" -ForegroundColor Gray
Write-Host "   - Adicione os 6 integrantes da equipe" -ForegroundColor Gray
Write-Host "3. 🧪 Testar uma das opções (Django/Flask)" -ForegroundColor White
Write-Host "4. 📝 Documentar credenciais para a equipe" -ForegroundColor White
Write-Host ""

Write-Host "🔗 Acesse seu repositório em:" -ForegroundColor Green
$repoWebUrl = $repoUrl -replace "\.git$", ""
Write-Host "$repoWebUrl" -ForegroundColor Cyan
Write-Host ""

Read-Host "Pressione Enter para finalizar"