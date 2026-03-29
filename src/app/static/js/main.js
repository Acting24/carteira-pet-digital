/**
 * Carteira Digital Pet - JavaScript Principal
 * PJI110 - UNIVESP 2026
 */

// Aguardar carregamento completo da página
document.addEventListener('DOMContentLoaded', function() {
    console.log('🐕 Carteira Digital Pet - Sistema carregado!');
    
    // Inicializar funcionalidades
    initializeApp();
    setupEventListeners();
    
    // Log de informações do sistema
    console.log('📊 Sistema:', {
        version: '1.0.0',
        framework: 'Flask',
        frontend: 'Bootstrap 5',
        timestamp: new Date().toISOString()
    });
});

/**
 * Inicializar aplicação
 */
function initializeApp() {
    // Mostrar toast de boas-vindas se for primeira visita
    if (!localStorage.getItem('visited')) {
        showWelcomeToast();
        localStorage.setItem('visited', 'true');
    }
    
    // Animar contadores se existirem
    animateCounters();
    
    // Configurar tooltips do Bootstrap
    initializeTooltips();
    
    // Verificar status da API
    checkAPIStatus();
}

/**
 * Configurar event listeners
 */
function setupEventListeners() {
    // Smooth scroll para âncoras
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Auto-dismiss alerts após 5 segundos
    document.querySelectorAll('.alert').forEach(alert => {
        if (alert.classList.contains('alert-dismissible')) {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        }
    });
    
    // Adicionar loading spinner aos botões de form
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Carregando...';
                submitBtn.disabled = true;
            }
        });
    });
}

/**
 * Mostrar toast de boas-vindas
 */
function showWelcomeToast() {
    // Criar toast dinamicamente
    const toastHTML = `
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="welcomeToast" class="toast" role="alert">
                <div class="toast-header">
                    <i class="fas fa-paw text-primary me-2"></i>
                    <strong class="me-auto">Carteira Digital Pet</strong>
                    <small>Agora</small>
                    <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
                </div>
                <div class="toast-body">
                    <div class="d-flex align-items-center">
                        <div class="me-3">
                            <i class="fas fa-rocket text-success fs-4"></i>
                        </div>
                        <div>
                            <strong>Bem-vindo ao sistema!</strong><br>
                            <small class="text-muted">O projeto está em desenvolvimento ativo.</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', toastHTML);
    
    const toastElement = document.getElementById('welcomeToast');
    const toast = new bootstrap.Toast(toastElement, {
        delay: 8000
    });
    toast.show();
    
    // Remover do DOM após dismiss
    toastElement.addEventListener('hidden.bs.toast', function() {
        this.parentElement.remove();
    });
}

/**
 * Animar contadores (se existirem)
 */
function animateCounters() {
    const counters = document.querySelectorAll('[data-count]');
    
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-count'));
        const duration = 2000; // 2 segundos
        const increment = target / (duration / 16); // 60 FPS
        let current = 0;
        
        const timer = setInterval(() => {
            current += increment;
            counter.textContent = Math.floor(current);
            
            if (current >= target) {
                counter.textContent = target;
                clearInterval(timer);
            }
        }, 16);
    });
}

/**
 * Inicializar tooltips do Bootstrap
 */
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Verificar status da API
 */
async function checkAPIStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        
        console.log('✅ API Status:', data);
        
        // Atualizar indicador de status se existir
        const statusIndicator = document.getElementById('api-status');
        if (statusIndicator) {
            statusIndicator.innerHTML = `
                <i class="fas fa-circle text-success me-1"></i>
                <small>API Online</small>
            `;
        }
        
    } catch (error) {
        console.error('❌ Erro ao verificar API:', error);
        
        const statusIndicator = document.getElementById('api-status');
        if (statusIndicator) {
            statusIndicator.innerHTML = `
                <i class="fas fa-circle text-danger me-1"></i>
                <small>API Offline</small>
            `;
        }
    }
}

/**
 * Utilitários gerais
 */
const PetUtils = {
    // Formatar data para padrão brasileiro
    formatDate: function(dateString) {
        return new Date(dateString).toLocaleDateString('pt-BR');
    },
    
    // Mostrar notificação
    showNotification: function(message, type = 'info') {
        const alertClass = type === 'error' ? 'alert-danger' : 
                          type === 'success' ? 'alert-success' : 'alert-info';
        
        const alertHTML = `
            <div class="alert ${alertClass} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3" style="z-index: 9999;" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `;
        
        document.body.insertAdjacentHTML('afterbegin', alertHTML);
        
        // Auto-remover após 5 segundos
        setTimeout(() => {
            const alert = document.querySelector('.alert');
            if (alert) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 5000);
    },
    
    // Copiar texto para área de transferência
    copyToClipboard: function(text) {
        navigator.clipboard.writeText(text).then(() => {
            this.showNotification('Texto copiado!', 'success');
        }).catch(() => {
            this.showNotification('Erro ao copiar texto', 'error');
        });
    },
    
    // Validar email
    isValidEmail: function(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    },
    
    // Debounce para search
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
};

// Expor utilitários globalmente
window.PetUtils = PetUtils;

/**
 * Event listeners para funcionalidades específicas
 */

// Copiar links de API quando clicados
document.addEventListener('click', function(e) {
    if (e.target.matches('a[href*="/api/"]')) {
        e.preventDefault();
        const url = window.location.origin + e.target.getAttribute('href');
        PetUtils.copyToClipboard(url);
    }
});

// Easter egg: Konami code
let konamiCode = [];
const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65]; // ↑ ↑ ↓ ↓ ← → ← → B A

document.addEventListener('keydown', function(e) {
    konamiCode.push(e.keyCode);
    
    if (konamiCode.length > konamiSequence.length) {
        konamiCode = konamiCode.slice(-konamiSequence.length);
    }
    
    if (JSON.stringify(konamiCode) === JSON.stringify(konamiSequence)) {
        activateEasterEgg();
        konamiCode = [];
    }
});

function activateEasterEgg() {
    // Adicionar chuva de patas
    const style = document.createElement('style');
    style.textContent = `
        @keyframes pawfall {
            0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
        }
        .paw-rain {
            position: fixed;
            top: -50px;
            font-size: 20px;
            animation: pawfall 3s linear;
            pointer-events: none;
            z-index: 9999;
        }
    `;
    document.head.appendChild(style);
    
    // Criar patas caindo
    for (let i = 0; i < 50; i++) {
        setTimeout(() => {
            const paw = document.createElement('div');
            paw.innerHTML = '🐾';
            paw.className = 'paw-rain';
            paw.style.left = Math.random() * 100 + 'vw';
            paw.style.animationDelay = Math.random() * 2 + 's';
            document.body.appendChild(paw);
            
            // Remover após animação
            setTimeout(() => paw.remove(), 3000);
        }, i * 100);
    }
    
    PetUtils.showNotification('🎉 Você encontrou o easter egg! Chuva de patas! 🐾', 'success');
}

// Log de desenvolvimento
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    console.log('%c🐕 Carteira Digital Pet - Modo Desenvolvimento', 
                'color: #ff6b6b; font-size: 16px; font-weight: bold;');
    console.log('📝 Dicas para desenvolvimento:');
    console.log('• Use PetUtils para funções utilitárias');
    console.log('• Todos os tooltips são inicializados automaticamente');
    console.log('• Alerts são auto-dismissed em 5 segundos');
    console.log('• Tente o Konami Code! ↑↑↓↓←→←→BA');
}