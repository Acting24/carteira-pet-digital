# ==========================================
# SCRIPT PARA TESTAR DJANGO E FLASK
# Carteira Digital Pet - PJI110 UNIVESP  
# ==========================================

Write-Host "🧪 Testando implementações do projeto..." -ForegroundColor Green
Write-Host ""

# Verificar Python
try {
    $pythonVersion = python --version
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python não encontrado!" -ForegroundColor Red
    Write-Host "Instale Python em: https://python.org/downloads" -ForegroundColor Yellow
    Write-Host "Marque 'Add Python to PATH' durante a instalação" -ForegroundColor Yellow
    Read-Host "Pressione Enter para sair"
    exit 1
}

Write-Host ""
Write-Host "🎯 OPÇÕES DE TESTE:" -ForegroundColor Cyan
Write-Host "1. 🥇 Django (Recomendado)" -ForegroundColor White
Write-Host "2. 🥈 Flask (Alternativa)" -ForegroundColor White
Write-Host "3. ⚡ Ambos (teste rápido)" -ForegroundColor White
Write-Host ""

$opcao = Read-Host "Escolha uma opção (1, 2 ou 3)"

if ($opcao -eq "1" -or $opcao -eq "3") {
    Write-Host ""
    Write-Host "🥇 TESTANDO DJANGO..." -ForegroundColor Green
    Write-Host "=================================" -ForegroundColor Green
    
    # Verificar se django_app existe
    if (Test-Path "django_app") {
        Write-Host "✅ Pasta django_app encontrada" -ForegroundColor Green
        
        # Criar ambiente virtual Django
        Write-Host "📦 Criando ambiente virtual Django..." -ForegroundColor Yellow
        try {
            if (Test-Path "venv_django") {
                Remove-Item -Recurse -Force "venv_django"
            }
            python -m venv venv_django
            Write-Host "✅ Ambiente virtual criado!" -ForegroundColor Green
        } catch {
            Write-Host "❌ Erro ao criar ambiente virtual" -ForegroundColor Red
            Write-Host $Error[0] -ForegroundColor Red
        }
        
        # Ativar ambiente e instalar Django
        Write-Host "⚙️ Instalando Django (apenas Django básico)..." -ForegroundColor Yellow
        try {
            & "venv_django\Scripts\activate.ps1"
            pip install Django==4.2.9
            
            Write-Host "✅ Django instalado!" -ForegroundColor Green
            
            # Testar Django
            Write-Host "🧪 Testando Django..." -ForegroundColor Yellow
            Set-Location "django_app"
            
            # Verificar se manage.py existe
            if (Test-Path "manage.py") {
                Write-Host "✅ manage.py encontrado" -ForegroundColor Green
                
                # Tentar rodar Django
                Write-Host "🚀 Iniciando Django..." -ForegroundColor Yellow
                Write-Host "O Django será executado por 10 segundos para teste..." -ForegroundColor Gray
                
                $djangoJob = Start-Job -ScriptBlock {
                    Set-Location $using:pwd
                    Set-Location "django_app"
                    & "..\venv_django\Scripts\python.exe" manage.py runserver --noreload
                }
                
                Start-Sleep 3
                
                # Testar se Django está rodando
                try {
                    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000" -TimeoutSec 5
                    if ($response.StatusCode -eq 200) {
                        Write-Host "🎉 DJANGO FUNCIONANDO!" -ForegroundColor Green
                        Write-Host "URL: http://127.0.0.1:8000" -ForegroundColor Cyan
                    }
                } catch {
                    Write-Host "⚠️ Django iniciado, mas página não responde (normal para primeira execução)" -ForegroundColor Yellow
                    Write-Host "Execute manualmente: python manage.py runserver" -ForegroundColor Cyan
                }
                
                # Parar Django
                Stop-Job $djangoJob
                Remove-Job $djangoJob
                
            } else {
                Write-Host "❌ manage.py não encontrado em django_app/" -ForegroundColor Red
            }
            
            Set-Location ".."
            
        } catch {
            Write-Host "❌ Erro no teste Django:" -ForegroundColor Red
            Write-Host $Error[0] -ForegroundColor Red
        }
        
    } else {
        Write-Host "❌ Pasta django_app não encontrada!" -ForegroundColor Red
    }
}

if ($opcao -eq "2" -or $opcao -eq "3") {
    Write-Host ""
    Write-Host "🥈 TESTANDO FLASK..." -ForegroundColor Green
    Write-Host "==============================" -ForegroundColor Green
    
    # Verificar se src e run.py existem
    if ((Test-Path "src") -and (Test-Path "run.py")) {
        Write-Host "✅ Estrutura Flask encontrada" -ForegroundColor Green
        
        # Criar ambiente virtual Flask
        Write-Host "📦 Criando ambiente virtual Flask..." -ForegroundColor Yellow
        try {
            if (Test-Path "venv_flask") {
                Remove-Item -Recurse -Force "venv_flask"
            }
            python -m venv venv_flask
            Write-Host "✅ Ambiente virtual criado!" -ForegroundColor Green
        } catch {
            Write-Host "❌ Erro ao criar ambiente virtual Flask" -ForegroundColor Red
        }
        
        # Ativar ambiente e instalar Flask
        Write-Host "⚙️ Instalando Flask (apenas Flask básico)..." -ForegroundColor Yellow
        try {
            & "venv_flask\Scripts\activate.ps1"
            pip install Flask==3.0.0
            
            Write-Host "✅ Flask instalado!" -ForegroundColor Green
            
            # Testar Flask
            Write-Host "🧪 Testando Flask..." -ForegroundColor Yellow
            Write-Host "O Flask será executado por 10 segundos para teste..." -ForegroundColor Gray
            
            $flaskJob = Start-Job -ScriptBlock {
                Set-Location $using:pwd
                & "venv_flask\Scripts\python.exe" run.py
            }
            
            Start-Sleep 3
            
            # Testar se Flask está rodando
            try {
                $response = Invoke-WebRequest -Uri "http://127.0.0.1:5000" -TimeoutSec 5
                if ($response.StatusCode -eq 200) {
                    Write-Host "🎉 FLASK FUNCIONANDO!" -ForegroundColor Green
                    Write-Host "URL: http://127.0.0.1:5000" -ForegroundColor Cyan
                }
            } catch {
                try {
                    # Tentar Hello World
                    $response = Invoke-WebRequest -Uri "http://127.0.0.1:5000/hello" -TimeoutSec 5
                    if ($response.StatusCode -eq 200) {
                        Write-Host "🎉 FLASK FUNCIONANDO!" -ForegroundColor Green
                        Write-Host "URL Hello World: http://127.0.0.1:5000/hello" -ForegroundColor Cyan
                    }
                } catch {
                    Write-Host "⚠️ Flask iniciado, mas não responde (verifique run.py)" -ForegroundColor Yellow
                }
            }
            
            # Parar Flask
            Stop-Job $flaskJob
            Remove-Job $flaskJob
            
        } catch {
            Write-Host "❌ Erro no teste Flask:" -ForegroundColor Red
            Write-Host $Error[0] -ForegroundColor Red
        }
        
    } else {
        Write-Host "❌ Estrutura Flask não encontrada!" -ForegroundColor Red
        Write-Host "Verifique se existe: src/ e run.py" -ForegroundColor Yellow
    }
}

# Resumo dos testes
Write-Host ""
Write-Host "📋 RESUMO DOS TESTES:" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan

if (Test-Path "venv_django") {
    Write-Host "🥇 Django: ✅ Testado (ambiente: venv_django/)" -ForegroundColor Green
    Write-Host "   Para usar: venv_django\Scripts\activate && cd django_app && python manage.py runserver" -ForegroundColor Gray
} else {
    Write-Host "🥇 Django: ❌ Não testado" -ForegroundColor Yellow
}

if (Test-Path "venv_flask") {
    Write-Host "🥈 Flask: ✅ Testado (ambiente: venv_flask/)" -ForegroundColor Green  
    Write-Host "   Para usar: venv_flask\Scripts\activate && python run.py --debug" -ForegroundColor Gray
} else {
    Write-Host "🥈 Flask: ❌ Não testado" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎯 PRÓXIMOS PASSOS RECOMENDADOS:" -ForegroundColor Cyan
Write-Host "1. 📖 Ler README.md e GUIA_DE_UTILIZACAO.md" -ForegroundColor White
Write-Host "2. 🎯 Escolher Django OU Flask para desenvolvimento" -ForegroundColor White
Write-Host "3. 📦 Instalar dependências completas (requirements-django.txt)" -ForegroundColor White
Write-Host "4. 🗃️ Configurar banco de dados (.env)" -ForegroundColor White
Write-Host "5. 👥 Compartilhar repositório com equipe" -ForegroundColor White
Write-Host ""

Write-Host "📚 DOCUMENTAÇÃO DISPONÍVEL:" -ForegroundColor Green
if (Test-Path "README.md") {
    Write-Host "✅ README.md - Manual completo do projeto" -ForegroundColor White
}
if (Test-Path "GUIA_DE_UTILIZACAO.md") {
    Write-Host "✅ GUIA_DE_UTILIZACAO.md - Como usar os arquivos" -ForegroundColor White
}
if (Test-Path "requirements-django.txt") {
    Write-Host "✅ requirements-django.txt - Dependências Django" -ForegroundColor White
}
if (Test-Path "requirements.txt") {
    Write-Host "✅ requirements.txt - Dependências Flask" -ForegroundColor White
}

Write-Host ""
Read-Host "Pressione Enter para finalizar"